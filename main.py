from core.git_utils import get_git_diff, create_fix_branch
from core.reviewer import review_diff
from core.tester import run_tests
from core.analyzer import analyze_error
from core.fixer import generate_fix
from core.utils import extract_file_from_diff
from core.apply_fix import apply_fix_to_file
import subprocess


def main():
    print("🚀 PyCI Guardian Started\n")

    # Step 1: Diff
    diff = get_git_diff()
    print("📄 Diff:\n", diff)

    if not diff.strip():
        print("No changes detected.")
        return

    print("\n📄 Diff detected\n")

    # Step 2: Review
    issues, ai_review = review_diff(diff)

    print("🔍 Issues:")
    for i in issues:
        print(f"❌ {i}")

    print("\n🤖 AI Review:\n", ai_review)

    # Step 3: Test
    print("\n🧪 Running tests...")
    result = run_tests()

    if result["success"]:
        print("✅ Tests Passed")
        return

    print("❌ Tests Failed")

    print("\n--- ERROR LOG ---")
    print(result["output"])

    # Step 4: Analyze
    error_type = analyze_error(result["output"])
    print(f"\n🧠 Error Type: {error_type}")

    # Step 5: Fix
    code, full_response = generate_fix(diff, result["output"])

    print("\n🔧 AI Fix Suggestion:\n")
    print(full_response)

    if code:
        user_input = input("\nApply fix automatically? (y/n): ")

        if user_input.lower() == "y":
            file_path = extract_file_from_diff(diff)

            if file_path:
                apply_fix_to_file(file_path, code)
            else:
                print("❌ Could not detect file to fix")
            create_fix_branch()

            subprocess.run(["git", "add", "."])
            subprocess.run(["git", "commit", "-m", "auto fix applied"])

            print("🚀 Auto fix committed!")

    else:
        print("⚠️ No valid code block found")


if __name__ == "__main__":
    main()
