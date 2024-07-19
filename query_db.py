from obtuariesproject.app import db, Obituary

def view_obituaries():
    obituaries = Obituary.query.all()
    for obituary in obituaries:
        print(f"ID: {obituary.id}")
        print(f"Name: {obituary.name}")
        print(f"Date of Birth: {obituary.date_of_birth}")
        print(f"Date of Death: {obituary.date_of_death}")
        print(f"Content: {obituary.content}")
        print(f"Author: {obituary.author}")
        print(f"Submission Date: {obituary.submission_date}")
        print("----------")

if __name__ == "__main__":
    view_obituaries()

