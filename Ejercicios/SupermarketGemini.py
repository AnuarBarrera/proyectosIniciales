class Supermarket:
    def __init__(self, num_boxes):
        self.pay_boxes = [[] for _ in range(num_boxes)]  # Initialize boxes as empty lists

    def add_customer(self, box_num):
        self.pay_boxes[box_num - 1].append("customer")
        print("Customer added to box", box_num)

    def serve_customer(self, box_num):
        if self.pay_boxes[box_num - 1]:
            self.pay_boxes[box_num - 1].pop(0)
            print("Customer served from box", box_num)
        else:
            print("No customers in box", box_num)

    def display_boxes(self):
        for i, box in enumerate(self.pay_boxes, 1):
            print(f"Box {i}: {box}")

if __name__ == "__main__":
    print("Welcome to the Supermarket")

    while True:
        menu = int(input("Choose an option:\n1. Open boxes\n2. Add customer\n3. Serve customer\n4. Display boxes\n5. Exit"))

        if menu == 1:
            num_boxes = int(input("Enter number of boxes: "))
            market = Supermarket(num_boxes)
            print("Supermarket opened with", num_boxes, "boxes")
        elif menu == 2:
            box_num = int(input("Enter box number: "))
            market.add_customer(box_num)
        elif menu == 3:
            box_num = int(input("Enter box number: "))
            market.serve_customer(box_num)
        elif menu == 4:
            market.display_boxes()
        elif menu == 5:
            break
        else:
            print("Invalid option")
