INSERT INTO "sped_roster" ("student_id", "has_iep", "has_504")
VALUES
((SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'lnford29@titanacademy.edu'), False,True),
((SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu'), True,True),
((SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'bmparker27@titanacademy.edu'), False,True),
((SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'babrown27@titanacademy.edu'), False,True),
((SELECT student_id FROM student WHERE email = 'krgarrison27@titanacademy.edu'), True,False),
((SELECT student_id FROM student WHERE email = 'rpdavis27@titanacademy.edu'), False,True);


INSERT INTO "sped_categories" ("sped_category")
VALUES
('Specific Learning Disabilities'),
('Other Health Impaired'),
('Speech And Language'),
('Autism'),
('Intellectual Disabilities'),
('Emotional Disturbance'),
('Multiple Disabilities'),
('Developmental Delay'),
('Hearing Impairments'),
('Traumatic Brain Injury'),
('Orthopedic Impairments'),
('Visual Impairments'),
('Deaf Blindness');


INSERT INTO "students_sped_categories" ("student_id", "category_id")
VALUES
((SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Speech And Language')),
((SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Autism')),
((SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Autism')),
((SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Intellectual Disabilities')),
((SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Autism')),
((SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Speech And Language')),
((SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Speech And Language')),
((SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Speech And Language')),
((SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Autism')),
((SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Traumatic Brain Injury')),
((SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Autism')),
((SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Autism')),
((SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Deaf Blindness')),
((SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Orthopedic Impairments')),
((SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Visual Impairments')),
((SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Emotional Disturbance')),
((SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Intellectual Disabilities')),
((SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Other Health Impaired')),
((SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Autism')),
((SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Other Health Impaired')),
((SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Other Health Impaired')),
((SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Orthopedic Impairments')),
((SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Other Health Impaired')),
((SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Other Health Impaired')),
((SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Intellectual Disabilities')),
((SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Specific Learning Disabilities')),
((SELECT student_id FROM student WHERE email = 'krgarrison27@titanacademy.edu'), (SELECT category_id FROM sped_categories WHERE sped_category = 'Traumatic Brain Injury'));

