INSERT INTO "staff" ("first_name", "middle_name", "last_name", "email", "position")
VALUES
('Samuel', 'Noah', 'Sanders', 'samuel.sanders@titanacademy.edu', '6th Grade Math Teacher'),
('Mackenzie', 'Krystal', 'Castaneda', 'mackenzie.castaneda@titanacademy.edu', '6th Grade Science Teacher, 6th Grade Level Chair'),
('Gregory', 'Adrian', 'Miller', 'gregory.miller@titanacademy.edu', '6th Grade History Teacher'),
('Kyle', 'George', 'Burke', 'kyle.burke@titanacademy.edu', '6th Grade Reading Teacher'),
('Stephanie', 'Alejandra', 'Saunders', 'stephanie.saunders@titanacademy.edu', '6th Grade Writing Teacher'),
('Bianca', 'Katie', 'Jones', 'bianca.jones@titanacademy.edu', '7th Grade Math Teacher'),
('Cassandra', 'Stephanie', 'Carter', 'cassandra.carter@titanacademy.edu', '7th Grade Science Teacher'),
('Krystal', 'Kirsten', 'Walton', 'krystal.walton@titanacademy.edu', '7th Grade History Teacher'),
('Timothy', 'Jonathon', 'Macdonald', 'timothy.macdonald@titanacademy.edu', '7th Grade Reading Teacher'),
('Jennifer', 'Selena', 'Taylor', 'jennifer.taylor@titanacademy.edu', '7th Grade Writing Teacher, 7th Grade Level Chair'),
('April', 'Laura', 'Evans', 'april.evans@titanacademy.edu', '8th Grade Math Teacher'),
('Angel', 'Leslie', 'Williams', 'angel.williams@titanacademy.edu', '8th Grade Science Teacher'),
('Rachael', 'Lindsay', 'Garrett', 'rachael.garrett@titanacademy.edu', '8th Grade History Teacher'),
('Raven', 'Diamond', 'Johnson', 'raven.johnson@titanacademy.edu', '8th Grade Reading Teacher'),
('Deanna', 'Jasmin', 'Austin', 'deanna.austin@titanacademy.edu', '8th Grade Writing Teacher, 8th Grade Level Chair');


INSERT INTO "grade_levels" ("grade_level_name", "grade_level_chair") VALUES
('6th Grade', (SELECT staff_id FROM staff WHERE email = 'mackenzie.castaneda@titanacademy.edu')),
('7th Grade', (SELECT staff_id FROM staff WHERE email = 'jennifer.taylor@titanacademy.edu')),
('8th Grade', (SELECT staff_id FROM staff WHERE email = 'deanna.austin@titanacademy.edu'));

INSERT INTO "staff_grade_levels" ("grade_level_id", "staff_id") VALUES
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade'), (SELECT staff_id FROM staff WHERE email = 'samuel.sanders@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade'), (SELECT staff_id FROM staff WHERE email = 'mackenzie.castaneda@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade'), (SELECT staff_id FROM staff WHERE email = 'gregory.miller@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade'), (SELECT staff_id FROM staff WHERE email = 'kyle.burke@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '6th Grade'), (SELECT staff_id FROM staff WHERE email = 'stephanie.saunders@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade'), (SELECT staff_id FROM staff WHERE email = 'bianca.jones@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade'), (SELECT staff_id FROM staff WHERE email = 'cassandra.carter@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade'), (SELECT staff_id FROM staff WHERE email = 'krystal.walton@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade'), (SELECT staff_id FROM staff WHERE email = 'timothy.macdonald@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '7th Grade'), (SELECT staff_id FROM staff WHERE email = 'jennifer.taylor@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '8th Grade'), (SELECT staff_id FROM staff WHERE email = 'april.evans@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '8th Grade'), (SELECT staff_id FROM staff WHERE email = 'angel.williams@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '8th Grade'), (SELECT staff_id FROM staff WHERE email = 'rachael.garrett@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '8th Grade'), (SELECT staff_id FROM staff WHERE email = 'raven.johnson@titanacademy.edu')),
((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '8th Grade'), (SELECT staff_id FROM staff WHERE email = 'deanna.austin@titanacademy.edu'));
