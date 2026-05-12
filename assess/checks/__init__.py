"""Check functions for AI Bug Automation Readiness Assessment."""

from .navigate import (
    check_build_setup,
    check_code_navigability,
    check_dependency_complexity,
    check_generated_code,
    check_type_safety,
)
from .submit import check_codeowners, check_contributing_guide, check_linting_in_ci, check_pr_template
from .understand import (
    check_agent_context,
    check_architecture_docs,
    check_bug_template,
    check_fixture_data,
    check_structured_logging,
)
from .verify import (
    check_ci_runs_tests,
    check_coverage_config,
    check_precommit_hooks,
    check_test_execution,
    check_test_isolation,
    check_test_ratio,
)

CHECK_FUNCTIONS = {
    "agent_context": check_agent_context,
    "bug_template": check_bug_template,
    "structured_logging": check_structured_logging,
    "architecture_docs": check_architecture_docs,
    "fixture_data": check_fixture_data,
    "code_navigability": check_code_navigability,
    "generated_code": check_generated_code,
    "build_setup": check_build_setup,
    "type_safety": check_type_safety,
    "dependency_complexity": check_dependency_complexity,
    "codeowners": check_codeowners,
    "test_ratio": check_test_ratio,
    "test_execution": check_test_execution,
    "coverage_config": check_coverage_config,
    "ci_runs_tests": check_ci_runs_tests,
    "test_isolation": check_test_isolation,
    "precommit_hooks": check_precommit_hooks,
    "pr_template": check_pr_template,
    "linting_in_ci": check_linting_in_ci,
    "contributing_guide": check_contributing_guide,
}

__all__ = [
    "CHECK_FUNCTIONS",
    "check_agent_context",
    "check_architecture_docs",
    "check_bug_template",
    "check_build_setup",
    "check_ci_runs_tests",
    "check_code_navigability",
    "check_codeowners",
    "check_contributing_guide",
    "check_coverage_config",
    "check_dependency_complexity",
    "check_fixture_data",
    "check_generated_code",
    "check_linting_in_ci",
    "check_pr_template",
    "check_precommit_hooks",
    "check_structured_logging",
    "check_test_execution",
    "check_test_isolation",
    "check_test_ratio",
    "check_type_safety",
]
