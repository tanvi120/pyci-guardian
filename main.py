import subprocess
import time
from core.watcher import start_watcher
from core.git_utils import get_git_diff, create_fix_branch
from core.reviewer import review_diff
from core.tester import run_tests
from core.analyzer import analyze_error
from core.fixer import generate_fix
from core.utils import extract_file_from_diff
from core.apply_fix import apply_fix_to_file
from core.github_pr import create_pull_request


def main():
    print("🚀 PyCI Guardian Started\n")

    # Step 1: Get diff
    diff = get_git_diff()

    if not diff.strip():
        print("No changes detected.")
        return

    print("📄 Diff detected (preview):\n")
    print("\n".join(diff.splitlines()[:20]))

    # Step 2: Review
    short_diff = diff[:800]
    issues, ai_review = review_diff(diff)

    print("\n🔍 Issues:")
    for issue in issues:
        print(f"❌ {issue}")

    print("\n🤖 AI Review:\n", ai_review)

    # Step 3: Run tests
    print("\n🧪 Running tests...")
    result = run_tests()

    if result["success"]:
        print("✅ Tests Passed")
        return

    print("❌ Tests Failed")

    # Step 4: Show error summary (last part only)
    error_output = result["output"]

    print("\n--- ERROR SUMMARY ---")
    print(error_output[-500:])

    # Step 5: Analyze error
    error_type = analyze_error(error_output)
    print(f"\n🧠 Error Type: {error_type}")

    # Step 6: Generate fix (limit input size for speed)
    short_diff = diff[:1000]
    short_error = error_output[:1000]

    code, full_response = generate_fix(short_diff, short_error)

    print("\n🔧 Fix generated (preview)")

    if not code:
        print("⚠️ No valid code block found from AI")
        return

    # Step 7: Ask user
    user_input = input("\nApply fix automatically? (y/n): ")

    if user_input.lower() != "y":
        print("Skipped auto-fix.")
        return

    # Step 8: Detect file
    file_path = extract_file_from_diff(diff)

    if not file_path:
        print("❌ Could not detect file to fix")
        return

    print(f"📁 Applying fix to: {file_path}")

    # Step 9: Apply fix
    apply_fix_to_file(file_path, code)

    # Step 10: Create unique branch
    branch_name = f"fix/auto-{int(time.time())}"

    create_fix_branch(branch_name)

    # Step 11: Commit changes
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "auto fix applied"])

    # Step 12: Push to GitHub
    push_result = subprocess.run(
        ["git", "push", "-u", "origin", branch_name],
        capture_output=True,
        text=True
    )

    if push_result.returncode != 0:
        print("❌ Push failed:\n", push_result.stderr)
        return

    print("🚀 Branch pushed to GitHub!")

    # Step 13: Create PR
    create_pull_request(branch_name)

    print("🎉 Auto fix PR created successfully!")


if __name__ == "__main__":
    print("🚀 PyCI Guardian Running (Background Mode)")
    start_watcher()
