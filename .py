class Exam:
    def __init__(self, name, department, duration, number_of_students):
        self.name = name
        self.department = department  # Department of students
        self.duration = duration
        self.number_of_students = number_of_students  # Number of students expected

class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

class Invigilator:
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability

def generate_schedule(exams, rooms, invigilators):
    schedule = []
    time_slots = ["9:00 AM", "11:00 AM", "1:00 PM"]  # Example time slots
    roll_number_start = 1000  # Starting roll number for students

    for exam in exams:
        for room in rooms:
            for invigilator in invigilators:
                # Check if the room can accommodate the number of students
                if room.capacity >= exam.number_of_students and invigilator.availability:
                    roll_number_end = roll_number_start + exam.number_of_students - 1  # Calculate end roll number
                    
                    # Check if time_slots is empty and handle the case
                    if not time_slots:  
                        print(f"Warning: No more time slots available for exam {exam.name}.")
                        break  # Break out of the invigilator loop if no time slots are available
                    
                    schedule.append({
                        "exam_name": exam.name,
                        "department": exam.department,  # Add department
                        "room_number": room.number,
                        "invigilator": invigilator.name,
                        "time_slot": time_slots[0],  # Assign first available time slot
                        "number_of_students": exam.number_of_students,  # Add number of students
                        "roll_number_range": f"{roll_number_start} - {roll_number_end}"  # Add roll number range
                    })
                    roll_number_start += exam.number_of_students  # Update starting roll number for next exam
                    time_slots.pop(0)  # Remove the assigned time slot
                    break  # Move to the next exam
            else:
                continue  # Only executed if the inner loop did NOT break
            break  # Break the outer loop if a room and invigilator were found
    return schedule

def display_schedule(schedule):
    print("\nGenerated Exam Schedule:")
    print("---------------------------------------------------")
    print(f"{'Exam Name':<20} {'Department':<15} {'Room Number':<15} {'Invigilator':<20} {'Time Slot':<15} {'Students':<10} {'Roll No. Range':<15}")
    print("---------------------------------------------------")
    for entry in schedule:
        print(f"{entry['exam_name']:<20} {entry['department']:<15} {entry['room_number']:<15} {entry['invigilator']:<20} {entry['time_slot']:<15} {entry['number_of_students']:<10} {entry['roll_number_range']:<15}")
    print("---------------------------------------------------")

def main():
    # Sample data
    exams = [
        Exam("Math 101", "Mathematics", 2, 25),
        Exam("Physics 101", "Physics", 2, 15),
        Exam("Chemistry 101", "Chemistry", 2, 20),
        Exam("Biology 101", "Biology", 2, 30)
    ]

    rooms = [
        Room("Room A", 30),
        Room("Room B", 20),
        Room("Room C", 25)
    ]

    invigilators = [
        Invigilator("John Doe", True),
        Invigilator("Jane Smith", True),
        Invigilator("Alice Johnson", True)
    ]

    # Generate and display the schedule
    schedule = generate_schedule(exams, rooms, invigilators)
    display_schedule(schedule)

if __name__ == "__main__":
    main()
