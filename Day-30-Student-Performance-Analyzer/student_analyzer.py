
import csv

INPUT_FILE = "students.csv"
OUTPUT_FILE = "report.csv"

SUBJECTS = ["python", "dbms", "web"]
PASS_MARKS = 35


def calculate_result(student):
    marks = [int(student[subject]) for subject in SUBJECTS]

    total = sum(marks)
    percentage = total / len(SUBJECTS)
    passed = all(mark >= PASS_MARKS for mark in marks)

    if not passed:
        grade = "F"
        status = "Fail"
    elif percentage >= 90:
        grade = "A+"
        status = "Pass"
    elif percentage >= 80:
        grade = "A"
        status = "Pass"
    elif percentage >= 70:
        grade = "B"
        status = "Pass"
    elif percentage >= 60:
        grade = "C"
        status = "Pass"
    else:
        grade = "D"
        status = "Pass"

    return {
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade,
        "status": status
    }


def analyze_students():
    try:
        with open(INPUT_FILE, "r", newline="",
                  encoding="utf-8") as file:
            students = list(csv.DictReader(file))

        if not students:
            print("No student records found.")
            return

        results = []

        for student in students:
            result = calculate_result(student)

            record = {
                "name": student["name"],
                "total": result["total"],
                "percentage": result["percentage"],
                "grade": result["grade"],
                "status": result["status"]
            }

            results.append(record)

            print(
                f"{record['name']}: "
                f"{record['percentage']}% | "
                f"Grade: {record['grade']} | "
                f"{record['status']}"
            )

        with open(OUTPUT_FILE, "w", newline="",
                  encoding="utf-8") as file:
            fields = [
                "name", "total", "percentage", "grade", "status"
            ]
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(results)

        passed = sum(
            1 for result in results
            if result["status"] == "Pass"
        )

        print("\n--- Class Summary ---")
        print("Total students:", len(results))
        print("Passed:", passed)
        print("Failed:", len(results) - passed)
        print(f"Class average: {sum(r['percentage'] for r in results) / len(results):.2f}%")
        print(f"\nReport saved to {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
    except (ValueError, KeyError) as error:
        print("Invalid student data:", error)


if __name__ == "__main__":
    analyze_students()
