from core.git_utils import get_git_diff, create_fix_branch
from core.reviewer import review_diff
from core.tester import run_tests
from core.analyzer import analyze_error
from core.fixer import generate_fix


def main():
    print("🚀 PyCI Guardian Started\n")

    # Step 1: Git diff
    diff = get_git_diff()
    print("📄 Diff content:\n", diff[:500])
    if not diff.strip():
        print("No changes detected.")
        return

    print("📄 Diff detected\n")

    # Step 2: Review
    issues, ai_review = review_diff(diff)

    print("🔍 Rule-Based Issues:")
    if issues:
        for issue in issues:
            print(f"❌ {issue}")
    else:
        print("✅ No rule issues")

    print("\n🤖 AI Review:")
    print(ai_review)

    # Step 3: Run tests
    print("\n🧪 Running tests...")
    result = run_tests()

    if result["success"]:
        print("✅ Tests Passed")
        return

    print("❌ Tests Failed")

    print("\n--- ERROR LOG ---")
    print(result["output"][:500])

    # Step 4: Analyze
    error_type = analyze_error(result["output"])
    print(f"\n🧠 Error Type: {error_type}")

    # Step 5: Fix suggestion
    fix = generate_fix(diff, result["output"])

    print("\n🔧 Suggested Fix:\n")
    print(fix)

    # Step 6: Create branch
    user_input = input("\nCreate fix branch? (y/n): ")

    if user_input.lower() == "y":
        create_fix_branch()
        print("✅ Created branch: fix/auto-fix")


if __name__ == "__main__":
    main()
