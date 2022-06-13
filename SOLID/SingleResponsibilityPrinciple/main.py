
from SOLID.SingleResponsibilityPrinciple.single_responsibility import Journal
from SOLID.SingleResponsibilityPrinciple.single_responsibility import PersistenceManager

if __name__ == "__main__":
    j = Journal()
    j.add_entry("I am sad today")
    j.add_entry("I ate bug")
    print(f"Journal entries :\n{j}")

    PersistenceManager.save_file(j, "journal.txt")
