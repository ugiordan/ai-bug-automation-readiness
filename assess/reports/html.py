"""HTML report generation with Chart.js visualizations."""

import html as html_mod
import json as json_mod
from datetime import datetime

from ..config import CHECKS
from ..engine import readiness_level
from . import prepare_report_data


# Unified color thresholds: 80+ green, 60+ amber, 40+ orange, <40 red
def _score_color(score):
    if score >= 80:
        return "#10B981"
    if score >= 60:
        return "#F59E0B"
    if score >= 40:
        return "#F97316"
    return "#EF4444"


def _render_summary_cards(d, prefix):
    """Render the summary cards section (Code Repos, Average Score, tiers)."""
    return f"""<div class="cards" role="region" aria-label="Score summary">
  <div class="card">
    <div class="value">{d['total_code']}<span style="font-size:1rem;color:#6B7280">/{d['total_code'] + d['total_noncode']}</span></div>
    <div class="label">Code Repos Assessed</div>
  </div>
  <div class="card">
    <div class="value">{d['avg']:.0f}<span style="font-size:1rem;color:#6B7280">/100</span></div>
    <div class="label">Average Score</div>
  </div>
  <div class="card">
    <div class="value" style="color:#10B981">{d['tier_counts']['Ready']}</div>
    <div class="label">Ready</div>
  </div>
  <div class="card">
    <div class="value" style="color:#B45309">{d['tier_counts']['Partially Ready']}</div>
    <div class="label">Partially Ready</div>
  </div>
  <div class="card">
    <div class="value" style="color:#C2410C">{d['tier_counts']['Needs Work']}</div>
    <div class="label">Needs Work</div>
  </div>
  <div class="card">
    <div class="value" style="color:#EF4444">{d['tier_counts']['Not Ready']}</div>
    <div class="label">Not Ready</div>
  </div>
</div>
"""


def _render_shortlist(d, prefix, org_prefix):
    """Render the Bug Bash Shortlist section (all 4 tiers)."""
    esc = html_mod.escape

    html = f"""<h2 id="{prefix}shortlist">Bug Bash Shortlist <a class="anchor" href="#{prefix}shortlist">#</a></h2>
<div class="shortlist">
  <h3 style="color:#10B981">Ready (score 80+) - {len(d['ready_repos'])} {'repo' if len(d['ready_repos']) == 1 else 'repos'}</h3>
  <ul>
"""
    for r in d["ready_repos"]:
        html += f'    <li><a href="https://github.com/{org_prefix}{esc(r["repo"])}" target="_blank">{esc(r["repo"])}</a> ({round(r["overall_score"])})</li>\n'
    if not d["ready_repos"]:
        html += "    <li>None yet</li>\n"

    html += f"""  </ul>
</div>
<div class="shortlist">
  <h3 style="color:#F59E0B">Partially Ready (score 60-79) - can start with some gaps ({len(d['partially_ready'])} {'repo' if len(d['partially_ready']) == 1 else 'repos'})</h3>
  <ul>
"""
    for r in d["partially_ready"]:
        checks_sorted = sorted([(k, v) for k, v in r["checks"].items() if not v.get("excluded")], key=lambda x: (100 - x[1]["score"]) * x[1]["weight"], reverse=True)
        top_action = esc(checks_sorted[0][1]["name"]) if checks_sorted else ""
        html += f'    <li><a href="https://github.com/{org_prefix}{esc(r["repo"])}" target="_blank">{esc(r["repo"])}</a> ({round(r["overall_score"])}) - top gap: {top_action}</li>\n'
    if not d["partially_ready"]:
        html += "    <li>None</li>\n"

    html += f"""  </ul>
</div>
<div class="shortlist">
  <h3 style="color:#F97316">Needs Work (score 40-59) - fix key gaps first ({len(d['needs_work'])} {'repo' if len(d['needs_work']) == 1 else 'repos'})</h3>
  <ul>
"""
    for r in d["needs_work"]:
        checks_sorted = sorted([(k, v) for k, v in r["checks"].items() if not v.get("excluded")], key=lambda x: (100 - x[1]["score"]) * x[1]["weight"], reverse=True)
        top_action = esc(checks_sorted[0][1]["name"]) if checks_sorted else ""
        html += f'    <li><a href="https://github.com/{org_prefix}{esc(r["repo"])}" target="_blank">{esc(r["repo"])}</a> ({round(r["overall_score"])}) - top gap: {top_action}</li>\n'
    if not d["needs_work"]:
        html += "    <li>None</li>\n"

    html += f"""  </ul>
</div>
<div class="shortlist">
  <h3 style="color:#EF4444">Not Ready (score &lt;40) - significant work needed ({len(d['not_ready'])} {'repo' if len(d['not_ready']) == 1 else 'repos'})</h3>
  <ul>
"""
    for r in d["not_ready"]:
        html += f'    <li><a href="https://github.com/{org_prefix}{esc(r["repo"])}" target="_blank">{esc(r["repo"])}</a> ({round(r["overall_score"])})</li>\n'
    if not d["not_ready"]:
        html += "    <li>None</li>\n"

    html += """  </ul>
</div>
"""
    return html


def _render_phases(d, prefix):
    """Render the Bug Fix Workflow Phases section."""
    phase_desc = {
        "Understand": "Can the agent understand the bug from the report and codebase context?",
        "Navigate": "Can the agent find the relevant code efficiently?",
        "Verify": "Can the agent run tests to verify the fix works?",
        "Submit": "Can the agent submit the fix following project conventions?",
    }
    phase_colors = {"Understand": "#8B5CF6", "Navigate": "#3B82F6", "Verify": "#10B981", "Submit": "#F59E0B"}

    html = f"""<h2 id="{prefix}phases">Bug Fix Workflow Phases <a class="anchor" href="#{prefix}phases">#</a></h2>
<p style="color:#6B7280;font-size:0.85rem;margin-bottom:1rem;">An AI agent fixing a bug goes through these phases. Scores show ecosystem average per phase.</p>
<div class="cards">
"""

    for phase in ["Understand", "Navigate", "Verify", "Submit"]:
        pavg = d["cat_avgs"].get(phase, 0)
        color = phase_colors.get(phase, "#6B7280")
        html += f"""  <div class="phase-card">
    <h3 style="color:{color}">{phase}</h3>
    <div class="phase-score" style="color:{color}">{pavg:.0f}/100</div>
    <div style="font-size:0.75rem;color:#6B7280;margin-top:0.25rem">{phase_desc.get(phase, '')}</div>
  </div>
"""

    html += """</div>
"""
    return html


def _render_scores_table(d, prefix):
    """Render the Repository Scores table."""
    esc = html_mod.escape

    html = f"""<h2 id="{prefix}scores">Repository Scores <a class="anchor" href="#{prefix}scores">#</a></h2>
<table>
<thead>
  <tr>
    <th>Repository</th>
    <th>Score</th>
    <th style="width:140px"></th>
    <th>Level</th>
    <th>Languages</th>
  </tr>
</thead>
<tbody>
"""

    for r in d["sorted_results"]:
        level, level_color = readiness_level(r["overall_score"])
        bar_w = int(round(r["overall_score"]) * 1.2)
        langs = ", ".join(r["languages"][:3])
        gate = ""
        if r.get("verify_gate"):
            gate = f' <span style="font-size:0.7rem;color:#EF4444">(verify gate applied)</span>'

        html += f"""  <tr>
    <td><a href="#{esc(r['repo'])}"><strong>{esc(r['repo'])}</strong></a>{gate}</td>
    <td><strong>{round(r['overall_score'])}</strong></td>
    <td><span class="bar-bg"><span class="bar" style="width:{bar_w}px;background:{level_color}"></span></span></td>
    <td><span class="badge" style="background:{level_color}">{level}</span></td>
    <td style="font-size:0.8rem;color:#6B7280">{esc(langs)}</td>
  </tr>
"""

    html += """</tbody>
</table>
"""
    return html


def _render_quick_wins(d, prefix):
    """Render the Quick Wins section."""
    esc = html_mod.escape

    if not d["quick_wins"]:
        return ""

    html = f"""<h2 id="{prefix}quick-wins">Quick Wins (Highest Impact Actions) <a class="anchor" href="#{prefix}quick-wins">#</a></h2>
<p style="color:#6B7280;font-size:0.85rem;margin-bottom:1rem;">Actions that would raise the most scores across the ecosystem, sorted by estimated impact.</p>
<table>
<thead><tr><th>Action</th><th>Repos Below 40</th><th>Weight</th><th>How to Fix</th></tr></thead>
<tbody>
"""
    for name, repos_below, lift, rec, weight in d["quick_wins"][:7]:
        html += f"""<tr>
  <td><strong>{esc(name)}</strong></td>
  <td>{repos_below} repos</td>
  <td>{weight}%</td>
  <td style="font-size:0.8rem">{esc(rec)}</td>
</tr>
"""
    html += "</tbody></table>\n"
    return html


def _render_how_scoring(d, prefix):
    """Render the How Scoring Works collapsible section."""
    esc = html_mod.escape

    html = f"""<details id="{prefix}how-scoring-works">
<summary style="cursor:pointer;font-weight:600;font-size:1.3rem;padding:0.5rem 0;color:#374151;border-bottom:2px solid #E5E7EB;margin-top:2.5rem">How Scoring Works <a class="anchor" href="#{prefix}how-scoring-works">#</a></summary>
<div style="margin-top:1rem;font-size:0.9rem;line-height:1.6;color:#4B5563">
<p>The overall score is a weighted average of {len(CHECKS)} checks, each scored 0-100. Checks are grouped into 4 phases of an AI bug-fixing workflow:</p>
<table style="margin:1rem 0;font-size:0.85rem">
<thead><tr><th>Phase</th><th>Weight</th><th>What it measures</th></tr></thead>
<tbody>
"""
    for phase in ["Understand", "Navigate", "Verify", "Submit"]:
        w = d["cat_weights"].get(phase, 0)
        checks_in_phase = [f'{c["name"]} ({c["weight"]}%)' for c in CHECKS.values() if c["category"] == phase]
        html += f"<tr><td><strong>{phase}</strong></td><td>{w}%</td><td>{', '.join(checks_in_phase)}</td></tr>\n"
    html += """</tbody></table>
<p><strong>Verify Phase Gate:</strong> If a repo's average Verify score is below 50, the overall score receives a smooth penalty multiplier that scales linearly from x0.4 (verify avg = 0) to x1.0 (verify avg = 50). This reflects that without test infrastructure, autonomous bug fixing is not viable.</p>
<p><strong>Readiness levels:</strong> Ready (80+), Partially Ready (60-79), Needs Work (40-59), Not Ready (&lt;40).</p>
</div>
</details>
"""
    return html


def _render_all_checks(d, prefix):
    """Render the All Checks Ranked collapsible section."""
    esc = html_mod.escape

    html = f"""<details id="{prefix}all-checks">
<summary style="cursor:pointer;font-weight:600;font-size:1.3rem;padding:0.5rem 0;color:#374151;border-bottom:2px solid #E5E7EB;margin-top:2.5rem">All Checks Ranked by Average Score <a class="anchor" href="#{prefix}all-checks">#</a></summary>
<table style="margin-top:1rem">
<thead><tr><th>Check</th><th>Avg Score</th><th style="width:140px"></th><th>Weight</th></tr></thead>
<tbody>
"""
    for cid, name, avg_score, weight in d["worst_checks"]:
        bar_w = int(avg_score * 1.2)
        bar_color = _score_color(avg_score)
        html += f"""<tr>
  <td>{esc(name)}</td><td>{avg_score:.0f}</td>
  <td><span class="bar-bg"><span class="bar" style="width:{bar_w}px;background:{bar_color}"></span></span></td>
  <td>{weight}%</td>
</tr>
"""
    html += "</tbody></table>\n</details>\n"
    return html


def _render_heatmap(d, prefix):
    """Render the Detailed Heatmap collapsible section."""
    esc = html_mod.escape

    html = f"""<details id="{prefix}heatmap">
<summary style="cursor:pointer;font-weight:600;font-size:1.3rem;padding:0.5rem 0;color:#374151;border-bottom:2px solid #E5E7EB;margin-top:2.5rem">Detailed Heatmap <a class="anchor" href="#{prefix}heatmap">#</a></summary>
<p style="color:#6B7280;font-size:0.85rem;margin:1rem 0">Green (80+) = ready, Yellow (40-79) = partial, Red (&lt;40) = gap.</p>
<div class="heatmap"><table><thead><tr><th>Repository</th><th>Score</th>
"""
    check_ids = list(CHECKS.keys())
    for cid in check_ids:
        name = CHECKS[cid]["name"]
        html += f'<th title="{esc(name)} ({CHECKS[cid]["weight"]}%)" style="writing-mode:vertical-lr;transform:rotate(180deg);height:140px;font-size:0.7rem;padding:4px 3px;">{esc(name)}</th>\n'
    html += "</tr></thead><tbody>\n"

    for r in d["sorted_results"]:
        html += f'<tr><td class="repo-col">{esc(r["repo"])}</td><td><strong>{round(r["overall_score"])}</strong></td>\n'
        for cid in check_ids:
            c = r["checks"].get(cid, {})
            if c.get("excluded"):
                html += '<td style="background:#E5E7EB;color:#9CA3AF;text-align:center;font-size:0.7rem">N/A</td>\n'
            else:
                s = c.get("score", 0)
                bg = "#D1FAE5" if s >= 80 else "#FEF3C7" if s >= 40 else "#FEE2E2"
                html += f'<td style="background:{bg}">{s:.0f}</td>\n'
        html += "</tr>\n"
    html += "</tbody></table></div>\n</details>\n"
    return html


def _render_per_repo(d, prefix, org_prefix):
    """Render the Per-Repository Details collapsible section."""
    esc = html_mod.escape
    check_ids = list(CHECKS.keys())

    html = f"""<details id="{prefix}per-repo">
<summary style="cursor:pointer;font-weight:600;font-size:1.3rem;padding:0.5rem 0;color:#374151;border-bottom:2px solid #E5E7EB;margin-top:2.5rem">Per-Repository Details <a class="anchor" href="#{prefix}per-repo">#</a></summary>
"""
    for r in d["sorted_results"]:
        level, level_color = readiness_level(r["overall_score"])
        profile_badge = ""
        if r.get("profile", {}).get("name", "default") != "default":
            p = r["profile"]
            profile_badge = f' <span class="badge" style="background:#6B7280;margin-left:4px">{esc(p["name"])}</span>'
        html += f"""<details id="{esc(r['repo'])}">
<summary>{esc(r['repo'])} <span class="badge" style="background:{level_color}">{round(r['overall_score'])}/100 - {level}</span>{profile_badge}</summary>
<table style="font-size:0.85rem">
<thead><tr><th>Check</th><th>Phase</th><th>Weight</th><th>Score</th><th>Evidence & Recommendation</th></tr></thead>
<tbody>
"""
        for cid in check_ids:
            c = r["checks"][cid]
            if c.get("excluded"):
                html += f"<tr style='color:#9CA3AF'><td>{c['name']}</td><td>{c['category']}</td><td>{c['weight']}%</td>"
                html += "<td>N/A</td><td><em>Excluded by profile</em></td></tr>\n"
            else:
                sc = _score_color(c["score"])
                ev = "<ul class='evidence'>" + "".join(f"<li>{esc(e)}</li>" for e in c["evidence"]) + "</ul>"
                rec_html = f"<div class='rec'>{esc(c['recommendation'])}</div>" if c.get("recommendation") else ""
                html += f"<tr><td>{c['name']}</td><td>{c['category']}</td><td>{c['weight']}%</td>"
                html += f"<td style='color:{sc};font-weight:600'>{c['score']:.0f}</td><td>{ev}{rec_html}</td></tr>\n"
        html += "</tbody></table></details>\n"
    html += "</details>\n"
    return html


def _render_excluded(d, prefix, org_prefix):
    """Render the Non-Code Repos Excluded section."""
    esc = html_mod.escape

    if not d["excluded_repos"]:
        return ""

    html = f"""<details id="{prefix}excluded">
<summary style="cursor:pointer;font-weight:600;font-size:1.3rem;padding:0.5rem 0;color:#374151;border-bottom:2px solid #E5E7EB;margin-top:2.5rem">Non-Code Repos Excluded ({len(d['excluded_repos'])}) <a class="anchor" href="#{prefix}excluded">#</a></summary>
<p style="color:#6B7280;font-size:0.9rem;margin:1rem 0">These repos contain no source code (docs, config, governance, etc.) and are excluded from scoring. AI bug-fix readiness assessment is not applicable to non-code repos.</p>
<ul style="column-count:3;column-gap:2rem;font-size:0.9rem;margin:1rem 0">
"""
    for r in d["excluded_repos"]:
        html += f'<li><a href="https://github.com/{org_prefix}{esc(r["repo"])}" target="_blank">{esc(r["repo"])}</a></li>\n'
    html += "</ul>\n</details>\n"
    return html


def _render_head(title, include_tabs=False):
    """Render the <head> section with all CSS (and optional tab CSS)."""
    tab_css = ""
    if include_tabs:
        tab_css = """  .tab-bar { display: flex; gap: 0; border-bottom: 2px solid #E5E7EB; margin-bottom: 2rem; overflow-x: auto; }
  .tab { padding: 0.6rem 1.25rem; border: none; background: none; font-size: 0.9rem; font-weight: 500; color: #6B7280; cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -2px; white-space: nowrap; }
  .tab:hover { color: #111827; }
  .tab.active { color: #2563EB; border-bottom-color: #2563EB; font-weight: 600; }
  .tab-all { margin-left: auto; }
  .tab-panel { display: none; }
  .tab-panel.active { display: block; }
  @media print { .tab-panel { display: block !important; page-break-before: always; } .tab-bar { display: none; } }
  @media (max-width: 768px) { .tab { padding: 0.5rem 0.75rem; font-size: 0.8rem; } }
"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #F9FAFB; color: #111827; padding: 2rem; max-width: 1400px; margin: 0 auto; }}
  h1 {{ font-size: 1.8rem; margin-bottom: 0.25rem; }}
  h2 {{ font-size: 1.3rem; margin: 2.5rem 0 1rem; color: #374151; border-bottom: 2px solid #E5E7EB; padding-bottom: 0.5rem; }}
  .subtitle {{ color: #6B7280; margin-bottom: 1rem; font-size: 0.9rem; }}
  .exec-summary {{ background: white; border-left: 4px solid #3B82F6; padding: 1rem 1.25rem; margin-bottom: 2rem; border-radius: 0 8px 8px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.1); font-size: 0.95rem; line-height: 1.6; }}
  .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem; margin-bottom: 2rem; }}
  .card {{ background: white; border-radius: 8px; padding: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); text-align: center; }}
  .card .value {{ font-size: 2rem; font-weight: 700; }}
  .card .label {{ font-size: 0.8rem; color: #6B7280; margin-top: 0.25rem; }}
  table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 2rem; }}
  th {{ background: #F3F4F6; text-align: left; padding: 0.75rem 1rem; font-size: 0.8rem; color: #374151; text-transform: uppercase; letter-spacing: 0.05em; }}
  td {{ padding: 0.6rem 1rem; border-top: 1px solid #E5E7EB; font-size: 0.9rem; }}
  tr:hover {{ background: #F9FAFB; }}
  .badge {{ display: inline-block; padding: 0.2rem 0.6rem; border-radius: 4px; color: white; font-size: 0.75rem; font-weight: 600; }}
  .bar-bg {{ display: inline-block; width: 120px; height: 8px; background: #E5E7EB; border-radius: 4px; }}
  .bar {{ display: inline-block; height: 8px; border-radius: 4px; }}
  .phase-card {{ background: white; border-radius: 8px; padding: 1rem 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  .phase-card h3 {{ font-size: 1rem; margin-bottom: 0.5rem; }}
  .phase-card .phase-score {{ font-size: 1.5rem; font-weight: 700; }}
  .evidence {{ font-size: 0.75rem; color: #6B7280; max-width: 400px; }}
  .evidence li {{ margin: 2px 0; }}
  .rec {{ font-size: 0.75rem; color: #2563EB; font-style: italic; margin-top: 4px; }}
  a {{ color: #2563EB; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .chart-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 2rem; }}
  .chart-card {{ background: white; border-radius: 8px; padding: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  @media (max-width: 768px) {{
    body {{ padding: 1rem; }}
    .cards {{ grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); }}
    .chart-grid {{ grid-template-columns: 1fr; }}
  }}
  .footer {{ margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #E5E7EB; color: #9CA3AF; font-size: 0.8rem; }}
  .heatmap {{ overflow-x: auto; }}
  .heatmap table {{ font-size: 0.8rem; }}
  .heatmap td {{ text-align: center; min-width: 45px; padding: 0.4rem 0.3rem; }}
  .heatmap .repo-col {{ text-align: left; font-weight: 600; white-space: nowrap; position: sticky; left: 0; background: white; z-index: 1; }}
  .heatmap thead th:first-child {{ position: sticky; left: 0; z-index: 2; }}
  .heatmap thead th:nth-child(2) {{ position: sticky; left: 0; z-index: 2; }}
  .shortlist {{ background: white; border-radius: 8px; padding: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 1rem; }}
  .shortlist h3 {{ font-size: 1rem; margin-bottom: 0.5rem; }}
  .shortlist ul {{ padding-left: 1.5rem; }}
  .shortlist li {{ margin: 4px 0; }}
  details {{ margin-bottom: 1rem; }}
  details summary {{ cursor: pointer; font-weight: 600; padding: 0.5rem 0; color: #374151; }}
  .anchor {{ color: #D1D5DB; text-decoration: none; font-weight: 400; padding-left: 0.3rem; }}
  .anchor:hover {{ color: #3B82F6; text-decoration: none; }}
  h2:hover .anchor {{ color: #9CA3AF; }}
  .toc {{ background: white; border-radius: 8px; padding: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 2rem; }}
  .toc ul {{ list-style: none; padding: 0; margin: 0; columns: 2; }}
  .toc li {{ margin: 4px 0; font-size: 0.9rem; }}
  @media (max-width: 768px) {{ .toc ul {{ columns: 1; }} }}
{tab_css}</style>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"
        integrity="sha384-NrKB+u6Ts6AtkIhwPixiKTzgSKNblyhlk0Sohlgar9UHUBzai/sgnNNWWd291xqt"
        crossorigin="anonymous"></script>
</head>
"""


def _render_charts_lazy(d, prefix):
    """Render chart canvases with data-chart attributes for lazy initialization."""
    esc = html_mod.escape

    score_bins = [0, 0, 0, 0, 0]
    for r in d["sorted_results"]:
        s = round(r["overall_score"])
        if s >= 80: score_bins[4] += 1
        elif s >= 60: score_bins[3] += 1
        elif s >= 40: score_bins[2] += 1
        elif s >= 20: score_bins[1] += 1
        else: score_bins[0] += 1

    bottleneck_counts = {"Understand": 0, "Navigate": 0, "Verify": 0, "Submit": 0}
    for r in d["sorted_results"]:
        phase_avgs = {}
        for c in r["checks"].values():
            if c.get("excluded"):
                continue
            phase_avgs.setdefault(c["category"], []).append(c["score"])
        phase_avgs = {p: sum(s)/len(s) for p, s in phase_avgs.items()}
        if phase_avgs:
            weakest = min(phase_avgs, key=phase_avgs.get)
            bottleneck_counts[weakest] = bottleneck_counts.get(weakest, 0) + 1

    gaps_labels = [name for _, name, _, _ in d["worst_checks"][:7]]
    gaps_scores = [round(avg_s, 1) for _, _, avg_s, _ in d["worst_checks"][:7]]
    gaps_colors = [_score_color(s) for s in gaps_scores]

    hist_config = json_mod.dumps({
        "type": "bar",
        "data": {
            "labels": ["0-19", "20-39", "40-59", "60-79", "80-100"],
            "datasets": [{
                "label": "Repos",
                "data": score_bins,
                "backgroundColor": ["#EF4444", "#F97316", "#F59E0B", "#84CC16", "#10B981"],
                "borderRadius": 4
            }]
        },
        "options": {
            "responsive": True,
            "plugins": {"legend": {"display": False}},
            "scales": {
                "y": {"beginAtZero": True, "ticks": {"stepSize": 1}},
                "x": {"title": {"display": True, "text": "Score Range"}}
            }
        }
    })

    gaps_config = json_mod.dumps({
        "type": "bar",
        "data": {
            "labels": gaps_labels,
            "datasets": [{
                "label": "Avg Score",
                "data": gaps_scores,
                "backgroundColor": gaps_colors,
                "borderRadius": 4
            }]
        },
        "options": {
            "indexAxis": "y",
            "responsive": True,
            "plugins": {"legend": {"display": False}},
            "scales": {
                "x": {"beginAtZero": True, "max": 100, "title": {"display": True, "text": "Average Score"}}
            }
        }
    })

    bn_config = json_mod.dumps({
        "type": "bar",
        "data": {
            "labels": list(bottleneck_counts.keys()),
            "datasets": [{
                "label": "Repos bottlenecked",
                "data": list(bottleneck_counts.values()),
                "backgroundColor": ["#8B5CF6", "#3B82F6", "#10B981", "#F59E0B"],
                "borderRadius": 4
            }]
        },
        "options": {
            "responsive": True,
            "plugins": {"legend": {"display": False}},
            "scales": {
                "y": {"beginAtZero": True, "ticks": {"stepSize": 1}, "title": {"display": True, "text": "Number of repos"}}
            }
        }
    })

    return f"""<h2 id="{prefix}score-overview">Score Overview <a class="anchor" href="#{prefix}score-overview">#</a></h2>
<div class="chart-grid">
  <div class="chart-card">
    <h3 style="font-size:0.95rem;margin-bottom:0.75rem;color:#374151">Score Distribution</h3>
    <canvas id="{prefix}histChart" height="200" role="img" aria-label="Histogram of repository score distribution" data-chart='{esc(hist_config)}'></canvas>
  </div>
  <div class="chart-card">
    <h3 style="font-size:0.95rem;margin-bottom:0.75rem;color:#374151">Biggest Gaps (Lowest Avg Scores)</h3>
    <canvas id="{prefix}gapsChart" height="200" role="img" aria-label="Bar chart of lowest-scoring checks" data-chart='{esc(gaps_config)}'></canvas>
  </div>
</div>
<div class="chart-grid" style="max-width:50%">
  <div class="chart-card">
    <h3 style="font-size:0.95rem;margin-bottom:0.75rem;color:#374151">Bottleneck Phases</h3>
    <p style="font-size:0.75rem;color:#6B7280;margin-bottom:0.5rem">Which phase is the weakest for each repo</p>
    <canvas id="{prefix}bottleneckChart" height="200" role="img" aria-label="Bar chart of bottleneck phases per repo" data-chart='{esc(bn_config)}'></canvas>
  </div>
</div>

"""


def _render_tab_script():
    """Return the tab-switching JavaScript for tabbed reports."""
    return """<script>
(function() {
  var tabs = document.querySelectorAll('.tab-bar .tab');
  var panels = document.querySelectorAll('.tab-panel');
  var chartInited = {};

  function switchTab(tabId) {
    tabs.forEach(function(t) {
      var active = t.getAttribute('data-tab') === tabId;
      t.classList.toggle('active', active);
      t.setAttribute('aria-selected', active ? 'true' : 'false');
    });
    panels.forEach(function(p) {
      var active = p.id === 'panel-' + tabId;
      p.classList.toggle('active', active);
    });
    history.replaceState(null, '', '#' + tabId);
    initChartsFor(tabId);
  }

  function initChartsFor(tabId) {
    if (chartInited[tabId]) return;
    chartInited[tabId] = true;
    var panel = document.getElementById('panel-' + tabId);
    if (!panel) return;
    panel.querySelectorAll('canvas[data-chart]').forEach(function(el) {
      new Chart(el, JSON.parse(el.getAttribute('data-chart')));
    });
  }

  tabs.forEach(function(t) {
    t.addEventListener('click', function() { switchTab(t.getAttribute('data-tab')); });
  });

  function handleHash() {
    var hash = location.hash.slice(1);
    if (!hash) return;
    if (document.getElementById('panel-' + hash)) {
      switchTab(hash);
      return;
    }
    var sep = hash.indexOf('--');
    if (sep > 0) {
      var org = hash.substring(0, sep);
      if (document.getElementById('panel-' + org)) {
        switchTab(org);
        setTimeout(function() {
          var target = document.getElementById(hash);
          if (target) {
            var el = target;
            while (el) { if (el.tagName === 'DETAILS') el.open = true; el = el.parentElement; }
            target.scrollIntoView();
          }
        }, 50);
      }
    }
  }

  document.addEventListener('click', function(e) {
    var a = e.target.closest('a[href^="#"]');
    if (!a) return;
    var target = document.getElementById(a.getAttribute('href').slice(1));
    if (!target) return;
    var panel = target.closest('.tab-panel');
    if (panel) switchTab(panel.id.replace('panel-', ''));
    var el = target;
    while (el) { if (el.tagName === 'DETAILS') el.open = true; el = el.parentElement; }
  });

  window.addEventListener('hashchange', handleHash);
  if (tabs.length > 0) {
    var hash = location.hash.slice(1);
    var initial = hash && document.getElementById('panel-' + hash) ? hash
      : (hash.indexOf('--') > 0 ? hash.substring(0, hash.indexOf('--')) : null);
    if (initial && document.getElementById('panel-' + initial)) {
      switchTab(initial); handleHash();
    } else {
      switchTab(tabs[0].getAttribute('data-tab'));
    }
  }
})();
</script>
"""


def generate_html_tabbed(results_by_org, title="AI Bug Automation Readiness Report"):
    """Generate multi-org tabbed HTML report."""
    esc = html_mod.escape
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    total_repos = sum(len(v) for v in results_by_org.values())

    # Build per-org data
    org_data = {}
    for org_name, org_results in results_by_org.items():
        org_data[org_name] = prepare_report_data(org_results, org=org_name)

    html = _render_head(esc(title), include_tabs=True)

    html += f"""<body>
<h1>{esc(title)}</h1>
<p class="subtitle">{total_repos} repositories across {len(results_by_org)} orgs &middot; {now}</p>

<nav class="tab-bar" role="tablist">
"""
    # Tab buttons
    first = True
    for org_name in results_by_org:
        d = org_data[org_name]
        active = " active" if first else ""
        selected = "true" if first else "false"
        html += f'  <button class="tab{active}" data-tab="{esc(org_name)}" role="tab" aria-selected="{selected}">{esc(org_name)} ({d["total_code"]})</button>\n'
        first = False
    html += '  <button class="tab tab-all" data-tab="all" role="tab" aria-selected="false">All Orgs</button>\n'
    html += '</nav>\n'

    # Per-org panels (each is a full independent analysis)
    first = True
    for org_name in results_by_org:
        d = org_data[org_name]
        prefix = f"{org_name}--"
        org_prefix = f"{org_name}/"
        active = " active" if first else ""

        html += f'<div class="tab-panel{active}" id="panel-{esc(org_name)}" role="tabpanel">\n'
        html += _render_summary_cards(d, prefix)
        html += _render_shortlist(d, prefix, org_prefix)
        html += _render_charts_lazy(d, prefix)
        html += _render_phases(d, prefix)
        html += _render_scores_table(d, prefix)
        html += _render_quick_wins(d, prefix)
        html += _render_how_scoring(d, prefix)
        html += _render_all_checks(d, prefix)
        html += _render_heatmap(d, prefix)
        html += _render_per_repo(d, prefix, org_prefix)
        html += _render_excluded(d, prefix, org_prefix)
        html += '</div>\n'
        first = False

    # "All" tab - cross-org comparison only
    html += '<div class="tab-panel" id="panel-all" role="tabpanel">\n'
    html += '<h2>Cross-Org Comparison</h2>\n'
    html += '<table>\n<thead><tr><th>Org</th><th>Repos</th><th>Avg Score</th><th>Ready</th><th>Partially Ready</th><th>Needs Work</th><th>Not Ready</th></tr></thead>\n<tbody>\n'
    for org_name in results_by_org:
        d = org_data[org_name]
        html += f'<tr><td><strong>{esc(org_name)}</strong></td><td>{d["total_code"]}</td><td>{d["avg"]:.0f}</td>'
        html += f'<td>{d["tier_counts"]["Ready"]}</td><td>{d["tier_counts"]["Partially Ready"]}</td>'
        html += f'<td>{d["tier_counts"]["Needs Work"]}</td><td>{d["tier_counts"]["Not Ready"]}</td></tr>\n'
    html += '</tbody></table>\n'

    # Cross-org bar chart (lazy init via data-chart)
    chart_config = json_mod.dumps({
        "type": "bar",
        "data": {
            "labels": list(results_by_org.keys()),
            "datasets": [{
                "label": "Average Score",
                "data": [round(org_data[o]["avg"], 1) for o in results_by_org],
                "backgroundColor": [_score_color(org_data[o]["avg"]) for o in results_by_org],
                "borderRadius": 4
            }]
        },
        "options": {"responsive": True, "plugins": {"legend": {"display": False}},
                    "scales": {"y": {"beginAtZero": True, "max": 100}}}
    })
    html += f'<div class="chart-card" style="max-width:600px;margin:2rem 0">\n'
    html += f'  <h3 style="font-size:0.95rem;margin-bottom:0.75rem;color:#374151">Average Score by Org</h3>\n'
    html += f"  <canvas id=\"all--orgChart\" height=\"200\" data-chart='{esc(chart_config)}'></canvas>\n"
    html += '</div>\n</div>\n'

    html += _render_tab_script()

    html += f"""<div class="footer">
  <p>AI Bug Automation Readiness Report &middot; Generated {now}</p>
</div>
</body></html>"""

    return html


def generate_html(all_results, title="AI Bug Automation Readiness Report", org=None):
    if not all_results:
        return "<html><body><h1>No repositories found to assess.</h1></body></html>"
    esc = html_mod.escape

    d = prepare_report_data(all_results, org=org)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    org_prefix = esc(d["org_prefix"])
    title = esc(title)
    prefix = ""

    # Bottleneck phase: which phase is the weakest for each repo
    bottleneck_counts = {"Understand": 0, "Navigate": 0, "Verify": 0, "Submit": 0}
    for r in d["sorted_results"]:
        phase_avgs = {}
        for c in r["checks"].values():
            if c.get("excluded"):
                continue
            phase_avgs.setdefault(c["category"], []).append(c["score"])
        phase_avgs = {p: sum(s)/len(s) for p, s in phase_avgs.items()}
        if phase_avgs:
            weakest = min(phase_avgs, key=phase_avgs.get)
            bottleneck_counts[weakest] = bottleneck_counts.get(weakest, 0) + 1

    # Score distribution for histogram
    score_bins = [0, 0, 0, 0, 0]  # 0-19, 20-39, 40-59, 60-79, 80-100
    for r in d["sorted_results"]:
        s = round(r["overall_score"])
        if s >= 80: score_bins[4] += 1
        elif s >= 60: score_bins[3] += 1
        elif s >= 40: score_bins[2] += 1
        elif s >= 20: score_bins[1] += 1
        else: score_bins[0] += 1

    noncode_note = f" ({d['total_noncode']} non-code repos excluded.)" if d.get('total_noncode') else ""
    exec_summary = (
        f"{d['ready_count']} of {d['total_code']} code repositories are partially ready or above for AI-assisted bug fixing.{noncode_note} "
        f"The ecosystem averages {d['avg']:.0f}/100. "
        f"The biggest gap is \"{d['biggest_gap'][1]}\" (avg {d['biggest_gap'][2]:.0f}/100) "
        f"which affects most repos and has high impact on AI agent success."
    )

    html = _render_head(title)

    html += f"""<body>

<h1>{title}</h1>
<p class="subtitle">{len(d['sorted_results'])} repositories assessed &middot; {now}</p>

<div class="exec-summary" role="region" aria-label="Executive summary">{esc(exec_summary)}</div>

<nav class="toc">
  <strong>Contents</strong>
  <ul>
    <li><a href="#shortlist">Bug Bash Shortlist</a></li>
    <li><a href="#score-overview">Score Overview</a></li>
    <li><a href="#phases">Workflow Phases</a></li>
    <li><a href="#scores">Repository Scores</a></li>
    <li><a href="#quick-wins">Quick Wins</a></li>
    <li><a href="#how-scoring-works">How Scoring Works</a></li>
    <li><a href="#all-checks">All Checks Ranked</a></li>
    <li><a href="#heatmap">Detailed Heatmap</a></li>
    <li><a href="#per-repo">Per-Repository Details</a></li>
    <li><a href="#excluded">Non-Code Repos Excluded</a></li>
  </ul>
</nav>

"""

    html += _render_summary_cards(d, prefix)
    html += "\n"
    html += _render_shortlist(d, prefix, org_prefix)
    html += "\n"
    html += f"""<h2 id="score-overview">Score Overview <a class="anchor" href="#score-overview">#</a></h2>
<div class="chart-grid">
  <div class="chart-card">
    <h3 style="font-size:0.95rem;margin-bottom:0.75rem;color:#374151">Score Distribution</h3>
    <canvas id="histChart" height="200" role="img" aria-label="Histogram of repository score distribution"></canvas>
  </div>
  <div class="chart-card">
    <h3 style="font-size:0.95rem;margin-bottom:0.75rem;color:#374151">Biggest Gaps (Lowest Avg Scores)</h3>
    <canvas id="gapsChart" height="200" role="img" aria-label="Bar chart of lowest-scoring checks"></canvas>
  </div>
</div>
<div class="chart-grid" style="max-width:50%">
  <div class="chart-card">
    <h3 style="font-size:0.95rem;margin-bottom:0.75rem;color:#374151">Bottleneck Phases</h3>
    <p style="font-size:0.75rem;color:#6B7280;margin-bottom:0.5rem">Which phase is the weakest for each repo</p>
    <canvas id="bottleneckChart" height="200" role="img" aria-label="Bar chart of bottleneck phases per repo"></canvas>
  </div>
</div>

"""

    html += _render_phases(d, prefix)
    html += "\n"
    html += _render_scores_table(d, prefix)
    html += _render_quick_wins(d, prefix)
    html += _render_how_scoring(d, prefix)
    html += _render_all_checks(d, prefix)
    html += _render_heatmap(d, prefix)
    html += _render_per_repo(d, prefix, org_prefix)
    html += _render_excluded(d, prefix, org_prefix)

    # Chart.js data and scripts
    gaps_labels = json_mod.dumps([name for _, name, _, _ in d["worst_checks"][:7]])
    gaps_scores = json_mod.dumps([round(avg_s, 1) for _, _, avg_s, _ in d["worst_checks"][:7]])
    hist_data = json_mod.dumps(score_bins)
    bn_labels = json_mod.dumps(list(bottleneck_counts.keys()))
    bn_data = json_mod.dumps(list(bottleneck_counts.values()))

    html += f"""
<script>
(function() {{
  function scoreColor(s) {{
    if (s >= 80) return '#10B981';
    if (s >= 60) return '#F59E0B';
    if (s >= 40) return '#F97316';
    return '#EF4444';
  }}

  const histCtx = document.getElementById('histChart');
  if (histCtx) {{
    new Chart(histCtx, {{
      type: 'bar',
      data: {{
        labels: ['0-19', '20-39', '40-59', '60-79', '80-100'],
        datasets: [{{
          label: 'Repos',
          data: {hist_data},
          backgroundColor: ['#EF4444', '#F97316', '#F59E0B', '#84CC16', '#10B981'],
          borderRadius: 4
        }}]
      }},
      options: {{
        responsive: true,
        plugins: {{ legend: {{ display: false }} }},
        scales: {{
          y: {{ beginAtZero: true, ticks: {{ stepSize: 1 }} }},
          x: {{ title: {{ display: true, text: 'Score Range' }} }}
        }}
      }}
    }});
  }}

  const gapsCtx = document.getElementById('gapsChart');
  if (gapsCtx) {{
    const gapsData = {gaps_scores};
    new Chart(gapsCtx, {{
      type: 'bar',
      data: {{
        labels: {gaps_labels},
        datasets: [{{
          label: 'Avg Score',
          data: gapsData,
          backgroundColor: gapsData.map(s => scoreColor(s)),
          borderRadius: 4
        }}]
      }},
      options: {{
        indexAxis: 'y',
        responsive: true,
        plugins: {{ legend: {{ display: false }} }},
        scales: {{
          x: {{ beginAtZero: true, max: 100, title: {{ display: true, text: 'Average Score' }} }}
        }}
      }}
    }});
  }}

  const bnCtx = document.getElementById('bottleneckChart');
  if (bnCtx) {{
    new Chart(bnCtx, {{
      type: 'bar',
      data: {{
        labels: {bn_labels},
        datasets: [{{
          label: 'Repos bottlenecked',
          data: {bn_data},
          backgroundColor: ['#8B5CF6', '#3B82F6', '#10B981', '#F59E0B'],
          borderRadius: 4
        }}]
      }},
      options: {{
        responsive: true,
        plugins: {{ legend: {{ display: false }} }},
        scales: {{
          y: {{ beginAtZero: true, ticks: {{ stepSize: 1 }}, title: {{ display: true, text: 'Number of repos' }} }}
        }}
      }}
    }});
  }}
}})();

// Auto-expand collapsed details when navigating via anchor links
document.addEventListener('click', function(e) {{
  const a = e.target.closest('a[href^="#"]');
  if (!a) return;
  const id = a.getAttribute('href').slice(1);
  const target = document.getElementById(id);
  if (!target) return;
  let el = target;
  while (el) {{
    if (el.tagName === 'DETAILS') el.open = true;
    el = el.parentElement;
  }}
}});
</script>

<script>
(function() {{
  function openTarget() {{
    var id = location.hash.slice(1);
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    var node = el;
    while (node) {{
      if (node.tagName === 'DETAILS') node.open = true;
      node = node.parentElement;
    }}
    el.scrollIntoView();
  }}
  window.addEventListener('hashchange', openTarget);
  window.addEventListener('DOMContentLoaded', openTarget);
}})();
</script>

<div class="footer">
  <p>AI Bug Automation Readiness Report &middot; Generated {now}</p>
</div>
</body></html>"""
    return html
