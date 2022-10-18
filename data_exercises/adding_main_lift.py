# import csv
#
#
# def add_lift_version():
#     with open('main_lifts.csv', mode='a', newline='') as csvfile:
#         add_lift = str(input('Add lift: '))
#         add_version = str(input('Add version: '))
#         fieldnames = ['Lifts', 'Version']
#         writing = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writing.writeheader()
#         writing.writerow({'Lifts': 'SQUAT', 'Version': 'LOW-BAR'})
#         if len(add_lift) > 0 or len(add_version) > 0:
#             writing.writerow({f"Lifts": f"{add_lift}", 'Version': f"{add_version}"})
#         else:
#             pass
#
#
