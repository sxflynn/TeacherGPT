INSERT INTO "staff" ("first_name", "middle_name", "last_name", "email", "position")
VALUES
('Haley', 'Claudia', 'Mccarthy', 'haley.mccarthy@titanacademy.edu', '6th Grade Math Teacher'),
('Eric', 'Hector', 'Foster', 'eric.foster@titanacademy.edu', '6th Grade Science Teacher'),
('Scott', 'Kevin', 'Arias', 'scott.arias@titanacademy.edu', '6th Grade History Teacher, 6th Grade Level Chair'),
('Faith', 'Emma', 'Woods', 'faith.woods@titanacademy.edu', '6th Grade Reading Teacher'),
('Lauren', 'Marisa', 'Griffin', 'lauren.griffin@titanacademy.edu', '6th Grade Writing Teacher'),
('Scott', 'Douglas', 'Johnson', 'scott.johnson@titanacademy.edu', '7th Grade Math Teacher'),
('Alexis', 'Joanna', 'Savage', 'alexis.savage@titanacademy.edu', '7th Grade Science Teacher, 7th Grade Level Chair'),
('Dakota', 'Nicolas', 'Hurst', 'dakota.hurst@titanacademy.edu', '7th Grade History Teacher'),
('Mary', 'Paige', 'Wilkins', 'mary.wilkins@titanacademy.edu', '7th Grade Reading Teacher'),
('Taylor', 'Madison', 'Steele', 'taylor.steele@titanacademy.edu', '7th Grade Writing Teacher'),
('Clayton', 'Carlos', 'Newman', 'clayton.newman@titanacademy.edu', '8th Grade Math Teacher, 8th Grade Level Chair'),
('Shannon', 'Amy', 'Short', 'shannon.short@titanacademy.edu', '8th Grade Science Teacher'),
('Elijah', 'Nathaniel', 'Orr', 'elijah.orr@titanacademy.edu', '8th Grade History Teacher');


INSERT INTO "grade_levels" ("grade_level_name", "grade_level_chair") VALUES
('6th Grade Team', (SELECT staff_id FROM staff WHERE email = 'scott.arias@titanacademy.edu')),
('7th Grade Team', (SELECT staff_id FROM staff WHERE email = 'alexis.savage@titanacademy.edu')),
('8th Grade Team', (SELECT staff_id FROM staff WHERE email = 'clayton.newman@titanacademy.edu'));

INSERT INTO "staff_grade_levels" ("grade_level_id", "staff_id") VALUES
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'haley.mccarthy@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'eric.foster@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'scott.arias@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'faith.woods@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'lauren.griffin@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'scott.johnson@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'alexis.savage@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'dakota.hurst@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'mary.wilkins@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'taylor.steele@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '8th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'clayton.newman@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '8th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'shannon.short@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '8th Grade Team'), (SELECT staff_id FROM staff WHERE email = 'elijah.orr@titanacademy.edu'));
