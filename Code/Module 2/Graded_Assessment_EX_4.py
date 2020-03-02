# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:30:25 2020
Students in a class receive their grades as Pass/Fail. 
Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". 
In addition, scores above 95 (not included) are graded as "Top Score". 
Fill in this function so that it returns the proper grade.
@author: Ragib Shahariar Ayon
"""

def exam_grade(score):
	if score>95:
		grade = "Top Score"
	elif score>=60 :
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail