import os

# Name the file will be sved tasks inside 
FILE_NAME = "tasks.txt"

def load_tasks():
    """دالة لقراءه المهام المخزنه في الملف عند فتح البرنامج """
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf_8") as file:
        return [line.strip() for line in file.readlines()]


def save_tasks(tasks):
    """دالة لحفظ المهام داخل الملف النصي تلقائيا"""
    
    with open(FILE_NAME, "w", encoding="utf_8") as file:
        for task in tasks:
            file.write(f"{task}\n")
                
def main():
    # تحميل المهام القديمه من الملف فور تشغيل البرنامج 
    
    tasks = load_tasks()
    
    while True:
        print("\nمنظم إدارة المهام")
        print("1.عرض المهام الحاليه ")
        print("2.إضافة مهمه جديدة")
        print("3.حذف مهمة")
        print("4.خروج من البرنامج")
        
        choice = input("(1-4) اختر من رقم ").strip()
        
        if choice == '1':
            if not tasks:
                print("\nلا توجد مهام حاليه")
            else:
                print("\nقائمه مهماتك الحاليه: ")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}.{task}")
        
        elif choice == '2':
            new_task = input("\nاكتب المهمه التي تريد اضافتها:").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"\nتم اضافه'{new_task}'وحفظها بنجاح ")       
        
        elif choice == '3':
            if not tasks:
                print("\nلا توجد مهام لحذفها ")
            else:
                print("\nقائمة المهام ")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}.{task}")
                try:
                    task_num = int(input("\nادخل رقم المهمة التي تريد حذفها: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"تم حذف المهمة:'{removed}'وتحديث الحفظ ")
                    else:
                        print("رقم غير صحيح ")
                except ValueError:
                    print("الرجاء إدخال رقم صحيح ")
        
        elif choice == '4':
            print("\nشكرا لإستخدامك البرنامج، تم حفظ مهامك ")
            break
        else:
            print("خيار غير صحيح، حاول مره اخري. ")                        
if __name__ =="__main__":
    main()                
   