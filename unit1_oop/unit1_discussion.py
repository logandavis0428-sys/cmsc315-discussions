
"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    case_category = "General Legal Matter"

    def __init__(self, client_name, case_number):
        self.client_name = client_name
        self.case_number = case_number

    def display_info(self):
        print(f"Client Name: {self.client_name}")
        print(f"Case Number: {self.case_number}")
        print(f"Case Category: {self.case_category}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    case_category = "Solar Contract Dispute"
    department = "Solar Contract Review"

    def __init__(self, client_name, case_number, solar_provider, case_status):
        super().__init__(client_name, case_number)
        self.solar_provider = solar_provider
        self.case_status = case_status
        self.documents = {
            "contracts": [],
            "billing_statements": []
        }

    # Student-created extension: document tracking with input validation.
    def add_document(self, category, document_name):
        if category not in self.documents:
            print(f"Invalid document category: {category}")
            return

        if not isinstance(document_name, str) or not document_name.strip():
            print("Document name cannot be empty.")
            return

        self.documents[category].append(document_name.strip())
        print(f"Added document: {document_name.strip()}")

    # Override the parent class method to show additional case details.
    def display_info(self):
        super().display_info()
        print(f"Solar Provider: {self.solar_provider}")
        print(f"Case Status: {self.case_status}")
        print(f"Documents: {self.documents}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    case_one = ChildClass("Client A", "SC-101", "GoodLeap", "Under Review")
    case_two = ChildClass("Client B", "SC-102", "Sunrun", "Negotiations")

    print("\nClass variable accessed through the class:")
    print(ChildClass.department)

    print("\nSame class variable accessed through an object:")
    print(case_one.department)

    # This attribute is added only to case_one.
    case_one.priority = "High"

    print("\nFirst object's instance namespace:")
    print(case_one.__dict__)

    print("\nSecond object's instance namespace:")
    print(case_two.__dict__)

    print("\nChild class namespace:")
    print(ChildClass.__dict__)

    print("\nDoes the second object have a priority attribute?")
    print("priority" in case_two.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original_case = ChildClass(
        "Client C", "SC-103", "EverBright", "Document Collection"
    )

    original_case.add_document("contracts", "Solar Purchase Agreement")
    original_case.add_document("billing_statements", "January Statement")

    shallow_case = copy(original_case)
    deep_case = deepcopy(original_case)

    # A shallow copy creates a new outer object but keeps references
    # to the same nested mutable data, including the document lists.
    #
    # A deep copy creates independent copies of the nested data.
    # Changes to the original document lists will not affect it.

    original_case.documents["contracts"].append("Loan Agreement")

    print("\nOriginal object after modification:")
    print(original_case.documents)

    print("\nShallow copy after original was modified:")
    print(shallow_case.documents)

    print("\nDeep copy after original was modified:")
    print(deep_case.documents)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    general_case = ParentClass("Client D", "LC-100")
    general_case.display_info()

    print("\n=== Child Object ===")
    solar_case = ChildClass(
        "Client E", "SC-104", "GoodLeap", "Initial Review"
    )

    solar_case.add_document("contracts", "Solar Installation Agreement")
    solar_case.add_document("billing_statements", "February Statement")

    # Test the student-created extension with invalid input.
    solar_case.add_document("contracts", "")

    # This calls the overridden method, which also uses
    # the parent class's display_info() method.
    solar_case.display_info()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
