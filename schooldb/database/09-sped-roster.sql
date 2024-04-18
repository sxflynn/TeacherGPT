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


BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu'), 'Helen Moore''s Individual Education Program (IEP) is designed to support her unique learning needs due to her diagnosis of Specific Learning Disabilities, with a particular focus on dyslexia and associated challenges in reading comprehension, math reasoning, and writing skills. To facilitate Helen''s progress in these areas, she will receive differentiated instruction tailored to her learning profile, including multisensory reading programs to enhance her decoding and comprehension skills, and explicit instruction in mathematical reasoning. Writing instruction will focus on both mechanics and organization, employing graphic organizers and process writing techniques. Learning strategies, including self-monitoring and executive functioning skills, will be integrated across subjects. Helen will participate in both individual and small group sessions with a special education teacher twice a week for 45 minutes each session, while ongoing evaluations will inform adjustments to her educational plan.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Improve reading fluency and comprehension levels by 15% as measured by standardized reading assessments and classroom performance by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Enhance math reasoning skills, aiming for a 20% improvement in problem-solving and computational accuracy as assessed by unit tests and teacher observations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Advance writing skills, targeting a 25% increase in writing organization and mechanics as documented through a portfolio of classroom assignments and standardized writing tasks.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Provide extended time on all district and statewide assessments to ensure Helen has sufficient time to process and respond to test items.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Allow the use of a word processor during writing assessments to help mitigate mechanical difficulties and focus on composition quality.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Administer tests in a distraction-reduced setting to support concentration and performance.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu'), 'Damien Adams, a sixth-grade student diagnosed under the Speech and Language category, will receive a tailored IEP focusing on improving his articulation, expressive and receptive language skills, and the effective use of communication aids. Special education services will include bi-weekly sessions with a speech-language pathologist aimed at enhancing clarity and fluency of speech. Additionally, classroom instruction will integrate tools and strategies to support expressive language, including structured language exercises and peer interaction practices. Receptive language goals will be addressed through listening comprehension activities and teacher-led discussions, which will also assist in enriching his academic participation and understanding across subject areas. Speech therapy services will include individual and small-group sessions, which will utilize a combination of direct instruction, modeling, and practice using various communication aids to facilitate more effective classroom interaction and learning.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'Damien will demonstrate improved speech clarity and fluency, aiming for at least a 40% reduction in articulation errors as measured by standardized speech assessments and continuous performance recordings.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'To enhance Damien’s expressive language skills, he will engage in daily language activities, targeting a 30% increase in his ability to construct complex sentences and communicate abstract ideas effectively, as monitored by classroom assessments and speech pathologist evaluations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'Develop Damien’s receptive language skills by incorporating structured listening activities that will increase his comprehension of verbal instructions and peer interactions by at least 25%, assessed through oral and written comprehension tests.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'Provide extended time of up to 50% on both district and statewide assessments to accommodate processing needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'Damien will have access to a speech-to-text device during exams to assist with written responses, ensuring his understanding and knowledge are accurately reflected.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'Test instructions will be delivered orally and visually, with opportunities for repetition and clarification to ensure Damien fully understands assessment requirements.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu'), 'Lucy Mendoza''s Individual Education Program (IEP) is tailored to support her needs in the areas of social skills, behavioral interventions, sensory processing, communication strategies, and routine stability, given her diagnosis of Autism. To enhance her social skills, Lucy will participate in small group interactions twice a week, which will help her engage more comfortably in peer activities. Behavioral interventions will include a positive reinforcement plan to encourage appropriate classroom behaviors, monitored weekly by her support team. For sensory processing, Lucy will have access to a quiet space equipped with sensory tools to help her manage sensory overload throughout the school day. Her communication strategies will be supported through the use of visual aids and a speech-language pathologist who will work with her during bi-weekly sessions. Routine stability will be ensured by providing Lucy with a clear and consistent daily schedule, which will be visually displayed in her classroom and reviewed with her every morning.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Lucy will demonstrate improved peer interaction skills by participating in structured group activities, aiming to engage with peers four times during each session, as documented by the session facilitator.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Lucy will display positive classroom behavior, increasing her instances of positive interactions by 20% by the end of the semester, as recorded by her teachers using a behavioral chart.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Lucy will use the designated quiet area to effectively manage sensory overload, with a 50% reduction in sensory-related disruptions noted in her daily behavior log.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Lucy will increase her ability to express her needs and ideas clearly using visual aids, as measured by improved scores on the communication scale used by her speech-language therapist.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Lucy will follow her visual daily schedule independently 90% of the time, with progress monitored by her homeroom teacher.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Extended time on all district and statewide assessments to ensure Lucy is not rushed, providing her the opportunity to fully demonstrate her knowledge.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Access to a quiet testing environment to minimize sensory overload and distractions during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Permission to use visual aids during tests, which will assist Lucy in understanding test instructions and expressing her answers more effectively.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Provision of breaks during testing, allowing Lucy to manage fatigue and sensory input, which will help maintain her concentration and performance.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu'), 'Irene Romero''s Individual Education Program (IEP) focuses on specialized instruction and supports addressing her needs within the autism spectrum, particularly concentrating on social skills enhancement, behavioral adaptations, sensory processing support, improving communication strategies, and maintaining routine stability. In the realm of social skills, Irene will participate in small group sessions twice a week to develop appropriate social interactions and peer relationships under the guidance of a special education teacher and a school psychologist. Behavioral interventions will encompass consistent positive reinforcement techniques and the use of a visual schedule to help Irene understand expectations and reduce anxiety. For sensory issues, Irene will have access to a quiet space equipped with sensory tools (e.g., stress balls, noise-cancelling headphones) to manage sensory overload and improve focus. Communication skills will be targeted through weekly speech therapy sessions, where Irene will learn to use augmentative and alternative communication (AAC) tools effectively. Routine stability will be ensured by maintaining a consistent daily schedule, highlighted by visual outlines to assist Irene in anticipating upcoming activities and transitions.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Improve Irene''s ability to initiate and maintain conversations with peers and adults, increasing her social interaction episodes by 50% by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Develop and implement behavioral strategies that decrease episodes of disruptive behavior by 40%, as measured by behavioral tracking sheets and teacher observations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Increase Irene''s sensory processing abilities to effectively use sensory tools to self-regulate during high-stress situations, measured by a 30% reduction in sensory-related disruptions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Enhance Irene''s communication skills, particularly in using AAC devices, leading to a 60% improvement in her ability to express needs, wants, and ideas clearly as tracked by speech therapy progress reports.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Maintain a structured and predictable environment for Irene, ensuring that daily visual schedules are consistently followed, with Irene demonstrating 90% adherence to routine transitions.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Provide extended time (time and a half) for district and statewide assessments to accommodate processing delays.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Administer tests in a small group setting to reduce anxiety and external sensory distractions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Use of an AAC device during tests, as needed, to assist in communicating answers effectively.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Offer breaks at regular intervals during testing to manage sensory processing and maintain focus.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu'), 'Warren Perry''s IEP focuses on enhancing his adaptive skills, functional academics, daily living activities, social development, and cognitive development. Despite his intellectual disabilities, Warren shows strong potential in academics as evidenced by his high grades. The IEP will include specialized instruction to develop his adaptive skills such as decision-making and problem-solving, tailored to his age and learning needs. Functional academics will be integrated with real-world applications to enhance his understanding and use of math and reading skills in everyday contexts. Daily living activities training will include structured tasks that promote independence, such as self-care and time management. Social development goals will focus on improving interactions with peers and adults, facilitated by a social skills training program. Cognitive development will be supported through strategies aimed at improving memory, attention, and reasoning skills. Services like speech therapy and occupational therapy will be provided as per the assessment, and progress will be measured through bi-monthly reviews and adapted as necessary to ensure optimal learning outcomes.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Improve adaptive skills by incorporating decision-making and problem-solving exercises into daily classroom activities, aiming for an improvement of at least 20% in situational assessments by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Enhance functional academics by applying math and reading skills to real-life scenarios such as budgeting activities and reading comprehension of real-life texts, with a goal to increase functional understanding by 25% as measured by task-based assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Increase independence in daily living activities through structured instruction in personal care and organizational skills, targeting a 30% reduction in required prompts for task completion.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Develop social communication skills by participating in a weekly peer interaction group and a social skills training program, aiming to achieve a 50% increase in positive peer interactions observed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Boost cognitive development through targeted cognitive exercises that emphasize memory, attention, and logical thinking, measuring progress through cognitive assessments every two months, targeting a 15% improvement.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Provide extended time for district and statewide assessments, allowing Warren a time increase of 50% beyond that given to his peers.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Administer tests in a small group setting to reduce distractions and enhance concentration, ensuring a more accurate reflection of Warren''s abilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Utilize technology-assisted reading during tests, including the use of text-to-speech software to facilitate comprehension and response accuracy.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Give visual aids and step-by-step breakdowns of exam instructions to help Warren understand test tasks more clearly and improve his ability to complete them accurately.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Allow breaks at necessary intervals to help Warren manage stress and fatigue, thereby maximizing his performance during assessments.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu'), 'Arnav Williams''s Individualized Education Program (IEP) is designed to address his specific learning disabilities, focusing on enhancing his skills in several key areas: dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. Arnav will receive specialized instruction in reading and writing through a multisensory approach that integrates visual, auditory, and kinesthetic learning strategies to improve his decoding and comprehension skills. For math, instruction will be tailored to develop his reasoning and problem-solving skills using concrete, pictorial, and abstract learning sequences to build a deep understanding of mathematical concepts. Arnav will also participate in sessions to improve his organizational and study skills, critical for overall academic success. Progress will be measured through continuous formative assessments and benchmark testing at the end of each quarter to ensure objectives are met and to adjust instruction as needed. Service frequency includes thrice-weekly sessions for reading and twice-weekly sessions for math and writing.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Improve reading comprehension skills to grade level by employing strategies to enhance decoding, fluency, and comprehension.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Develop math reasoning capabilities to interpret and solve grade-level problems correctly with at least 80% accuracy.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Enhance writing abilities to construct coherent paragraphs with minimal grammatical errors and proper structure.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Increase learning and organizational skills by implementing effective study techniques and utilizing graphic organizers to improve information retention.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Extended time on all district and statewide assessments (time and a half).'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Option to take tests in a quiet, distraction-free environment.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Use of text-to-speech software for reading assignments and examinations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Provision of formula sheets and graphic organizers for math tests.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Permission to record class sessions for later review and reinforcement of concepts.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu'), 'Braelyn Bauer''s IEP focuses on enhancing her abilities in several key developmental areas to support her educational growth. Recognizing her needs in social skills, the IEP includes targeted social interaction exercises and peer-group activities to boost her engagement and social comprehension. In behavioral interventions, Braelyn will receive support from a behavioral specialist to develop coping strategies for managing her sensory sensitivities, which will be integrated into her daily routines to encourage consistency and predictability in her school environment. Routine stability will be emphasized by maintaining a structured daily schedule, which will help reduce anxiety and support Braelyn''s focus and participation in class activities. Communication strategies will be strengthened through the use of visual aids and structured communication exercises to improve both her expressive and receptive language skills. Sensory processing strategies will concentrate on creating an adaptable learning environment that caters to her sensory needs, including the use of sensory tools like noise-canceling headphones and fidget toys.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Braelyn will improve her peer-to-peer interaction skills, demonstrated by participating in group activities and initiating interactions in 80% of opportunities as observed by her educators.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Braelyn will demonstrate improved coping strategies for managing sensory overload by utilizing taught techniques in 90% of observed instances where sensory triggers are present.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Braelyn will follow a structured routine with 95% accuracy, thereby reducing instances of behavioral distress related to transitions or unexpected changes.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Braelyn will increase her ability to express needs and ideas effectively using visual aids in 85% of communication opportunities, as recorded by her speech therapist.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Extended time on tests and assignments to accommodate processing speed and ensure comprehension, ensuring fairness in assessment conditions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Access to a quiet room or space during district and statewide assessments to manage sensory sensitivities and minimize distractions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Use of technology aids such as speech-to-text software during writing assessments to support communication and expression of ideas.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu'), 'Quentin Brown''s Individual Education Program (IEP) is designed to address his specific learning disabilities, with a strong focus on dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. Quentin will receive specialized instruction that includes structured literacy interventions tailored for dyslexia, which will utilize multisensory techniques to improve decoding and fluency. For reading comprehension, strategies will involve guided reading sessions and explicit instruction in understanding text structures and critical thinking. In math, Quentin will engage in problem-solving workshops and visual-spatial learning activities to enhance mathematical reasoning. Writing instruction will focus on the process approach, emphasizing planning, drafting, revising, and editing, supplemented by assistive technology tools to help Quentin organize his thoughts. Quentin''s learning strategies will incorporate executive function coaching, which will help him develop skills in organization, time management, and study strategies. The frequency of services will include thrice-weekly sessions for reading and math interventions, bi-weekly writing sessions, and weekly sessions for executive functioning skills development throughout the school year.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Quentin will improve reading fluency and accuracy skills to meet grade-level expectations, as measured by bi-monthly reading assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Increase Quentin''s ability to comprehend and interpret grade-level texts, achieving an 80% accuracy on standardized reading comprehension tests.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Enhance Quentin''s mathematical reasoning skills so that he can solve grade-appropriate problems with 75% accuracy, as measured by regular curriculum-based assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Develop Quentin''s writing skills to effectively organize and express ideas according to grade standards, with progress monitored through bi-weekly writing assignments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Quentin will apply executive function strategies to improve homework completion and test preparation, with a 50% reduction in missing assignments and late submissions.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Extended time on both district and statewide assessments (time and a half).'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Access to a quiet room for testing to reduce distractions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'The provision of text-to-speech software during exams to assist with reading comprehension.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Use of a calculator during math assessments when not testing basic calculation skills.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'The option to provide responses orally rather than in written form when possible during standardized testing.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu'), 'Arthur Kelley, a sixth-grade student diagnosed with Specific Learning Disabilities, presents strengths in several academic areas but faces challenges primarily in dyslexia and related reading comprehension tasks. Under his new IEP, Arthur will receive specialized instruction tailored to enhance his reading comprehension skills and address difficulties in math reasoning and writing coherence. Specifically, Arthur will participate in small group sessions twice a week focusing on structured literacy programs designed to bolster decoding and fluency. In math, his instruction will emphasize problem-solving strategies and conceptual understanding of mathematical principles. For writing, strategies to improve syntax and structure will be integrated into his curriculum. The IEP also incorporates learning strategies including graphic organizers and mnemonic devices to aid in information retention across all subjects. These interventions will be measured through bi-monthly progress monitoring to ensure Arthur achieves his IEP objectives effectively.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'To improve reading comprehension skills by 15% as measured by standardized reading assessments and teacher observations by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'To enhance math reasoning abilities, aiming for Arthur to independently solve grade-level word problems with 80% accuracy in bi-monthly assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'To develop writing coherence and structure, resulting in Arthur writing multi-paragraph essays that meet grade-level standards as evaluated through rubric-based assessments each semester.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'Extended time on district and statewide assessments (time and a half).'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'Option to use text-to-speech software for reading tasks during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'Access to formula sheets and visual aids during math assessments.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu'), 'Clare Clark''s Individualized Education Program (IEP) focuses on enhancing her capabilities in Speech and Language to ensure her continued success academically and socially. Given Clare''s strong academic performance, the IEP will primarily address her needs in Articulation, Expressive and Receptive Language, Communication Aids, and Speech Therapy. The program includes targeted speech therapy sessions twice a week to improve clarity and fluency of speech. Expressive language goals will focus on increasing Clare''s ability to construct complex sentences and improve her narrative skills, which will be integrated into her writing assignments. Receptive language enhancement will involve structured comprehension exercises during reading sessions. Additionally, the IEP will explore appropriate communication aids to support Clare''s in-class engagement and interactions. Progress will be measured through bi-monthly evaluations by the speech therapist and feedback from teachers across subjects.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Improve articulation skills to reduce phonological errors by 50% as measured by a speech pathologist using standard speech assessment tools.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Enhance expressive language skills to enable Clare to construct complex sentences and effectively use age-appropriate vocabulary in her written and oral communications.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Increase receptive language ability by incorporating structured comprehension exercises, aiming for a 30% improvement in understanding complex instructions and inferential questions in reading exercises.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Provide extended time on all district and statewide assessments to accommodate speech and language processing needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Allow for oral responses or use of communication aids in testing situations where written communication poses a challenge.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Ensure a quiet testing environment to minimize distractions and facilitate Clare''s concentration and speech processing.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu'), 'Allan Gibson''s Individualized Education Program (IEP) focuses on enhancing his speech and language skills, given his diagnosis in this category. A key objective for Allan is to improve articulation, allowing him to pronounce words more clearly and correctly in classroom discussions and social interactions. To achieve this, he will receive direct speech therapy twice per week from a certified speech-language pathologist. Furthermore, Allan''s expressive language skills will be targeted through structured group therapy sessions, where he will practice sentence structuring and vocabulary usage applicable to his curriculum content. This will also support his receptive language abilities as he engages with more complex instructions and peer interactions. Allan will also be introduced to various communication aids including speech-generating devices for augmentative communication under supervised conditions to bolster his autonomy in communication. Progress in these areas will be measured through regular assessments and speech therapy session observations documented by his speech-language pathologist.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will demonstrate clearer speech articulation by correctly pronouncing syllables and words through individual practice with minimal prompts in 4 out of 5 trials as measured by speech therapy progress logs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will increase his expressive language skills by constructing complex sentences and applying new vocabulary relevant to academic and social settings, as demonstrated in both structured group therapy sessions and classroom participation.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will improve in understanding and following multi-step instructions with 80% accuracy during classroom activities and therapy sessions, as logged by therapy and teacher observations.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will be given extended time (time and a half) to complete district and statewide assessments to accommodate processing needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Instructions for assessments will be provided both orally and in written form to support his comprehension abilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will be allowed to use a speech-to-text assistive technology during writing assignments and assessments to facilitate his written expression.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu'), 'Millie Galvan''s IEP is developed to address her needs in the areas of Articulation, Expressive Language, Receptive Language, and the use of Communication Aids. She will participate in tailored speech therapy sessions twice a week to improve clarity in her speech and broaden her vocabulary use in complex conversations. Each session aims to enhance her articulation skills using a variety of oral motor exercises and phonetic drills. Additionally, her program includes activities designed to further develop her expressive and receptive language abilities, enhancing her comprehension and ability to follow multi-step directions. Communication aids, including visual support tools, will be implemented in all her classroom settings to support her participation and comprehension in more complicated verbal interactions. Progress will be monitored through regular assessments and teacher observations to adjust the learning plans as needed.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'Millie will demonstrate improved articulation of sounds, achieving a 20% increase in clarity as measured by speech clarity scales during bi-monthly evaluations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'Millie will expand her expressive language skills by using more complex sentences and vocabulary in everyday communication, with progress being tracked through teacher assessments every two months.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'Millie will enhance her receptive language skills by accurately following multi-step instructions and understanding classroom lectures with minimal personal aid, as observed by teachers and recorded during end-of-term evaluations.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'Provide extended time (time and a half) for district and statewide assessments to accommodate language processing needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'Offer tests and instructions in both oral and written formats to support comprehension and expression in testing scenarios.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'Allow the use of speech-to-text technology during assessments to facilitate written responses.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu'), 'Cristopher Lowery’s IEP is designed to support his educational needs related to his autism diagnosis by focusing on social skills enhancement, behavioral interventions, sensory processing adjustments, effective communication strategies, and maintaining routine stability. Cristopher will participate in weekly sessions with a social skills group to improve peer interactions and understand social cues more effectively. Behavioral support will be provided by a specialized behavioral therapist who will work with Cristopher bi-weekly to develop coping strategies and positive reinforcement techniques that address specific challenges. Sensory friendly learning environments will be maintained to accommodate his sensory processing needs, which includes the use of sensory tools such as noise-cancelling headphones and fidget toys as needed during class and assessments. Communication strategies will be tailored through monthly sessions with a speech and language therapist to enhance both verbal and non-verbal communication skills. Stability in daily and weekly routines will be ensured by consistent scheduling and the use of visual daily schedules to help Cristopher manage transitions more effectively.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Improve peer-to-peer interaction and understanding of social norms by 20% as measured by teacher observations and social skills group feedback within the academic year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Develop and implement coping strategies that reduce instances of behavioral challenges by 30% as measured by behavioral incident reports and therapist assessments by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Enhance sensory processing by integrating at least three different sensory tools or strategies in the classroom distinctly documented in weekly teacher logs to manage sensory overload effectively throughout the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Increase proficiency in both verbal and non-verbal communication as reported in bi-monthly assessments by the speech and language therapist, aiming for a 25% improvement by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Consistently utilize a visual daily schedule and maintain a structured classroom environment to minimize anxiety around transitions, with a target of reducing transitional issues by 40% as observed by educators and reported quarterly.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Provide extended time on tests and assignments by 50% to accommodate processing and communication needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Use of a private room or minimal distraction environment for district and statewide assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Permission to use sensory tools such as noise-cancelling headphones and tactile fidgets during testing and class times to enhance focus and processing.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Allow breaks at necessary intervals during tests to manage stress and sensory overload, specifically after every 45 minutes of testing.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu'), 'Jeremiah Robinson''s Individual Education Program (IEP) is designed to address the unique challenges and educational needs arising from his Traumatic Brain Injury (TBI). The primary focus revolves around personalized cognitive rehabilitation strategies, the implementation of memory aids, continuous neurological assessments, consistent physical therapy, and behavioral adaptations aligned with his academic pursuits. Cognitive rehabilitation is tailored to improve Jeremiah''s problem-solving and executive functioning skills through bi-weekly sessions with a specialized neuropsychologist. Memory aids such as graphic organizers and digital voice recorders are integrated into all subjects to reinforce learning and retention. Monthly neurological assessments monitor cognitive enhancements and adapt interventions as necessary. Physical therapy sessions are scheduled twice a week to enhance motor skills and ensure physical adaptability, while his educators incorporate behavioral strategies to minimize any impulsive or distracted behaviors in the classroom, facilitating a conducive learning environment.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'To enhance Jeremiah''s problem-solving skills and executive functioning through personalized cognitive rehabilitation strategies and consistent monitoring.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'To ensure daily application of memory aids in all subjects, improving information retention and academic performance, while monitoring efficacy with quarterly evaluations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'To maintain and improve motor skills through bi-weekly physical therapy sessions and assess progress monthly to adjust strategies accordingly.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'To conduct monthly neurological assessments to monitor cognitive function and adjust therapeutic approaches as required.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'To implement and monitor behavioral adaptations in the classroom to enhance Jeremiah''s academic engagement and social interactions, with feedback sessions every two weeks.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Extended time on district and statewide tests to accommodate processing speed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Access to a quiet room for testing to minimize distractions and enhance focus.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Permission to use memory aids during tests, such as formula sheets or graphic organizers, to support information retrieval.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu'), 'Nathalie Coleman''s Individual Education Program (IEP) is designed to address challenges associated with Autism, such as difficulties in social interaction, behavioral regulation, sensory processing, and communication. To enhance her educational experience and meet her specific needs, Nathalie will receive tailored interventions and supports. Her IEP includes objectives for improving social skills through structured peer interaction activities twice weekly and a social skills training program facilitated by the school psychologist. For behavioral interventions, a behavior intervention plan (BIP) will be developed, focusing on positive reinforcement and clear, consistent consequences to encourage desirable behaviors. Sensory processing strategies will incorporate the use of sensory tools such as noise-cancelling headphones and fidget devices during classes to improve focus. Communication strategies will be strengthened by speech and language therapy sessions twice per week to enhance both expressive and receptive communication skills. To promote routine stability, Nathalie''s schedule will be highly structured, with visual schedules used to navigate transitions throughout the school day.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Improve Nathalie''s ability to initiate and maintain age-appropriate interactions with peers and adults, achieving a 50% increase in positive social interactions by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Develop and implement a behavior intervention plan that reduces instances of disruptive behavior by 40% within six months.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Enhance sensory processing abilities, allowing Nathalie to remain engaged in classroom activities for extended periods, with a decrease in sensory-related disruptions by 30%.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Increase proficiency in both expressive and receptive communication skills, aiming for a 25% improvement as measured by standardized speech therapy assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Maintain a consistent daily routine with visual supports to assist transitions, aiming for a 90% adherence rate to the scheduled routine.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Provide extended time, up to time and a half, on all district and statewide assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Allow for a smaller, quieter testing environment to reduce sensory overload and enhance focus during exams.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Offer the option to use technology aids such as a computer or tablet for test-taking to aid in communication and ease of writing.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Ensure all test instructions are clearly explained verbally and visually, with the opportunity to ask questions to clarify understanding.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu'), 'Yadiel Marsh''s IEP is designed to support his needs related to Specific Learning Disabilities, with a focus on dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. Yadiel displays strong academic performance, but requires tailored support in certain areas to sustain and enhance his learning outcomes. The program includes targeted progress in reading fluency and comprehension, mathematics reasoning, structured writing exercises, and effective learning strategies, facilitated by specialized instruction. Yadiel will receive direct instruction from a special education teacher in a small group setting twice a week for reading and math, and weekly sessions for writing and learning strategies. Instructional approaches will incorporate multisensory techniques, graphic organizers, and technology-assisted learning tools to enhance engagement and understanding.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Improve reading fluency and comprehension to a level that allows Yadiel to independently interpret grade-level texts and infer deeper meanings with 85% accuracy.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Enhance math reasoning skills to solve grade-level appropriate problems with increased precision and strategic approach, achieving an 80% success rate on problem-solving tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Develop structured writing skills enabling Yadiel to organize and express ideas clearly in written form, meeting grade-level standards with minimal errors in organization and grammar.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Master adaptive and compensatory learning strategies that facilitate independent learning and problem-solving in classroom settings, reducing reliance on external aids by 50%.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Provide extended time for district and statewide assessments to ensure Yadiel does not experience undue pressure and can demonstrate his true capabilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Allow use of a word processor during writing assessments to compensate for difficulties with manual writing and spelling due to dyslexia.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Administer tests in a small group setting to reduce distractions and provide a supportive testing environment, enhancing focus and performance.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu'), 'Raul Salazar’s Individualized Education Program (IEP) centers on enhancing his social skills, managing behavioral challenges, improving sensory processing and communication strategies, and maintaining routine stability. Raul will participate in small-group sessions twice a week focused on social skills training, where he will engage in role-playing, social stories, and guided interactions to improve his social communication and peer relationships. For behavioral interventions, Raul will work with a behavior specialist once a week to develop coping mechanisms and strategies for emotional regulation using a behavior intervention plan that incorporates positive reinforcements. Sensory processing support will be integrated daily through tailored activities that help him manage sensory sensitivities, and he will have access to sensory tools such as noise-canceling headphones and textured objects. Communication strategies will be reinforced through individual speech and language therapy sessions twice per month, focusing on pragmatic language skills and non-verbal communication cues. Routine stability will be supported by visual daily schedules and predictable, structured classroom environments.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Improve communication skills to effectively express needs, respond to questions, and participate in conversations with both adults and peers.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Develop and consistently use strategies for emotional regulation and behavior management, reducing instances of disruptive behavior by 50% over the next school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Increase ability to process and respond to sensory stimuli in various environments, with a goal of decreasing sensory-related disruptions by 40%.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Extended time on all district and statewide assessments, with a time extension of 50% beyond the time allocated to peers.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Provision of a quiet testing environment to reduce sensory overload during exams.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Permission to use a calculator and spell-check device during exams, irrespective of the normative requirements of the test.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu'), 'Jorge Morales'' Individualized Education Program (IEP) is crafted to address his unique needs stemming from Deaf Blindness. Emphasis will be placed on enhancing Jorge''s communication abilities through tactile communication methods and Braille Plus. Specialized instruction in Tactile Signing and Braille Plus will occur five times a week with a specialist to improve his ability to access written and communicated information. Orientation and mobility training will be provided thrice weekly to assist Jorge in safely navigating school environments. Further, assistive technologies, specifically tailored for dual sensory impairment, will be integrated into all his classes to promote independence and facilitate learning. Jorge will also engage in combined sensory strategies, which will include the use of adaptive devices such as refreshable Braille displays and auditory aids, coordinated by a team of occupational therapists and special educators.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'Demonstrate increased proficiency in tactile communication methods by correctly using tactile signing to interact with peers and teachers in a range of school settings, as measured by bi-monthly assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'Achieve mastery in the use of Braille Plus technology for all academic subjects, demonstrating a 50% improvement in reading and writing scores as indicated by monthly evaluations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'Independently navigate familiar and unfamiliar school environments using orientation and mobility skills acquired, with a reduction in assistance needed by 40%, as tracked through quarterly mobility assessments.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'Provide extended testing time up to 50% to accommodate slower reading and response due to dual sensory impairments during both district and statewide assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'Use of tactile graphics and Braille examination papers for all testing including district and statewide assessments to ensure accessibility.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'Access to an orientation and mobility specialist during assessments to facilitate effective navigation to and from the testing site.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu'), 'Edison Wyatt''s Individual Education Program (IEP) focuses on supporting his learning environment in accordance with his orthopedic impairments. Goals include enhancing his mobility within the school environment, ensuring he can access all necessary facilities, and improving his fine and gross motor skills. Edison will receive specialized instruction and services such as the use of adaptive equipment in the classroom to facilitate effective learning and participation. Daily physical therapy sessions are planned to strengthen his mobility, with additional monitoring of his adaptation to mobility aids, such as crutches or a wheelchair, as necessary. Regular assessments will be conducted to measure progress in his motor skills and the functionality of mobility aids.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'To increase Edison''s independence in navigating the school environment using his prescribed mobility aids with 90% efficiency by the end of the academic year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'To enhance Edison''s fine motor skills to improve his ability to perform school activities, such as writing and using a computer, with greater ease and less discomfort.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'To successfully integrate adaptive equipment into Edison''s daily classroom activities, ensuring all learning materials are accessible despite his physical limitations.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'Provide preferential seating arrangements to ensure Edison has optimal access and comfort in the classroom setting.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'Allow additional time for Edison to move between classes and use elevators or other mobility-supportive infrastructures as needed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'Modify district and statewide assessments environments to accommodate Edison’s physical needs, including the provision of adjustable desks, ergonomic seating options, and the use of technology to assist with writing and reading tasks if necessary.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu'), 'Sadie Bennett''s IEP is designed to support her educational needs due to her visual impairment. The program''s objectives are tailored to enhance her learning experience through the utilization of Braille, visual aids, orientation and mobility training, low vision aids, and ensuring all materials are accessible. Sadie will receive specialized instruction in Braille to improve her reading and writing fluency in this medium. Visual aids and low vision devices will be integrated into all her classroom activities to enhance her visual access to the curriculum. Additionally, orientation and mobility training will be provided to help Sadie navigate school environments safely and independently. All instructional materials, including textbooks and handouts, will be provided in accessible formats (large print, audio, or Braille) according to her preferences and needs. The IEP includes continuous evaluation of Sadie’s progress in these areas to ensure that adjustments are made as necessary, with assessments scheduled every trimester to monitor her achievements and areas needing further support.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Sadie will achieve a 90% proficiency in Braille literacy by the end of the school year, as measured by standardized tests designed for visually impaired students.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Sadie will independently navigate the school environment using her cane and orientation skills, with an improvement in her mobility skills by 75% as measured by the Orientation and Mobility Assessment.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Sadie will effectively use low vision aids in all her classes, demonstrating a 50% decrease in reported visual fatigue and a 30% increase in task completion speed as monitored by her teachers.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Provide all test materials in her preferred format of Braille or large print, with the option of audio recordings.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Allow extended time on all district and statewide assessments, up to time and a half of the standard allotted time.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Offer breaks during tests as needed to prevent fatigue, and provide tests in a distraction-reduced setting to accommodate visual processing requirements.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu'), 'Sage Lyons, a 7th-grade student diagnosed with Emotional Disturbance, requires a tailored educational approach focused on behavioral improvements, emotional regulation, and social skills enhancement. His IEP includes specific behavior goals aimed at reducing classroom disruptions and increasing task completion, which will be monitored through weekly observations and monthly behavioral assessments by school psychologists. Sage''s IEP also integrates bi-weekly counseling sessions to support emotional regulation and social interaction, addressing areas such as understanding and expressing emotions appropriately, and engaging positively with peers. A crisis plan is established, detailing immediate interventions and support practices to be used in situations where Sage exhibits acute emotional distress. This plan includes staff training on de-escalation techniques and steps for smoothly reintegrating Sage back into the classroom setting after an incident.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Improve classroom behavior by decreasing disruptions and increasing task completion rate by 40% as measured by teacher reports and monthly behavior tracking forms.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Develop emotional regulation skills by teaching Sage coping mechanisms to manage stress and anxiety, aiming for a 50% decrease in reported episodes of emotional distress.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Enhance social interaction skills by participating in structured peer group activities, leading to an improvement in peer relationships as evidenced by peer and teacher feedback.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Provide extended time (time and a half) on all district and statewide assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Allow breaks at regular intervals during testing and classroom activities to manage stress and maintain focus.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Use of a quiet room for testing to reduce anxiety and environmental distractions.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu'), 'Mariyah Martinez''s IEP is designed to support her educational needs associated with Specific Learning Disabilities, with a focus on Dyslexia, Reading Comprehension, Math Reasoning, Writing Skills, and Learning Strategies. Throughout the 7th grade, Mariyah will receive specialized instruction tailored to enhance her reading fluency and comprehension skills, addressing difficulties stemming from dyslexia. Her program includes structured literacy instruction delivered three times per week by a reading specialist, utilizing multisensory techniques proven effective for dyslexia. In math, Mariyah will receive strategic support to boost her reasoning skills through bi-weekly sessions that incorporate visual aids and practical applications to solidify concepts. For writing, targeted exercises to strengthen coherence and structure in her written expressions will be incorporated, facilitated by a language therapist. Skill-building in organizing and applying learned strategies across subjects will be continually integrated within all specialized service sessions.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'To improve Mariyah''s reading fluency and accuracy to grade level by implementing a structured literacy program that includes phonemic awareness, phonics, fluency, and vocabulary strategies suitable for students with dyslexia.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'To increase Mariyah''s reading comprehension skills to align with 7th grade benchmarks by providing tailored reading comprehension strategies that enhance her ability to understand and analyze text.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'To enhance Mariyah''s math reasoning capabilities to meet grade-level expectations through the use of manipulatives, visual aids, and problem-solving assignments that reinforce conceptual understanding.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'To develop Mariyah''s writing skills to grade level, focusing on organizing ideas and using appropriate grammatical structures, through weekly sessions with a language therapist specializing in writing strategies for students with learning disabilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'To coach Mariyah in applying effective learning strategies across all academic areas, ensuring she can independently organize, prioritize, and execute tasks related to her educational objectives.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'Extended time on all district and statewide assessments (time and a half) to accommodate processing speed challenges.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'Access to a word processor for written responses in exams to assist with writing challenges.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'Option to take exams in a small group setting to reduce anxiety and provide a distraction-reduced environment.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'Use of read-aloud accommodations for all assessments, including having instructions and questions read aloud by an adult or through assistive technology.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'The provision of visual aids and graphic organizers during tests to support comprehension and reasoning.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu'), 'Elle Maddox''s Individualized Education Program (IEP) is specifically designed to support her educational journey, with emphases on dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. Elle will receive specialized instruction aimed at enhancing her reading fluency and comprehension, crucial for her overall academic success given her dyslexia. Techniques including multisensory approaches and tailored reading interventions will be employed. In math, we will focus on developing her reasoning skills with the use of visual aids and real-world problem-solving scenarios. For writing, Elle will work with a specialist to improve her coherence and organization in writing tasks, utilizing graphic organizers and process writing approaches. Learning strategies will be incorporated across subjects to boost her independent learning skills and adaptative learning technologies will be used to support her specific learning needs. Her progress will be consistently monitored through a combination of standardized tests, class assignments, and regular feedback sessions.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Elle will improve her reading fluency and comprehension by one grade level by the end of the school year, as measured by teacher assessments and a standardized reading test.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Develop Elle''s math reasoning abilities to solve grade-level appropriate word problems with 80% accuracy, monitored through bimonthly math assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Enhance Elle''s writing skills to organize and articulate thoughts clearly in written form, with progress measured by comparing bi-monthly written assignments against a standard rubric.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Provide extended time for district and statewide assessments to ensure Elle has sufficient time to process questions and articulate her responses.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Use of text-to-speech software during tests and classroom assignments to aid reading comprehension and decrease reading fatigue.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Allow for breaks during tests to help manage fatigue, especially during longer assessment sessions.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu'), 'Izaiah Mills'' Individual Education Program (IEP) is designed to support his learning in areas affected by his Specific Learning Disabilities, particularly focusing on dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. To address his needs in reading and writing, Izaiah will participate in daily structured literacy sessions focusing on phonemic awareness, phonics, and syntax to improve decoding and encoding skills. In math, specialized instruction will target his conceptual understanding and problem-solving skills, with a focus on visual learning strategies and manipulatives. To enhance learning strategies, Izaiah will work with a special education teacher to develop organizational, time management, and study skills, important for across all subject areas. Progress will be monitored bi-weekly by assessments and quarterly IEP review meetings to ensure goals are being met and to adjust strategies as necessary.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Improve reading fluency and comprehension to a 5th-grade level as measured by standardized testing and in-class assessments by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Demonstrate improved math reasoning skills and ability to solve grade-level appropriate problems with minimal assistance, as evidenced by scoring 80% or higher on regular evaluations and class assignments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Enhance writing skills to effectively organize and express ideas in written form, achieving at least 80% in all writing assignments and projects through continuous feedback loops and revisions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Develop and consistently apply learning strategies that improve his ability to manage assignments in all academic subjects, as measured by teacher observations and a decrease in missing assignments.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Extended time on all district and statewide assessments (time and a half).'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Access to word processor with spell-check and text-to-speech software for writing tasks during exams.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Permission to give oral responses to written assessments or to use scribe as needed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Testing in a small group setting to reduce distractions.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu'), 'Nehemiah Glover''s Individual Education Program (IEP) is designed to enhance his abilities across various developmental domains considering his diagnosis of Intellectual Disabilities. Focused on both his academic performance and practical life skills, the program includes targeted objectives in adaptive skills, functional academics, daily living activities, social development, and cognitive growth. Nehemiah will receive specialized instruction tailored to his specific needs that encompass modified curriculum content, the use of assistive technologies, and the integration of communication strategies designed to improve understanding and expression. Moreover, consistent evaluations will be implemented to monitor Nehemiah''s progress, observed through a combination of teacher assessments, portfolio reviews, and standardized testing suited to his learning pace.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Improve Nehemiah''s mathematical reasoning and problem-solving skills to a proficiency level of 80% accuracy on adapted assessments, using tactile learning materials and visual aids.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Enhance Nehemiah''s reading comprehension skills by engaging him in daily reading activities and interactive story sessions aimed at increasing reading fluency to a satisfactory level as per age-appropriate standards.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Develop Nehemiah''s daily living skills by engaging him in structured tasks and situations to improve his ability to perform age-appropriate self-care routines independently by the end of the school year.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Provide extended time on all district and statewide assessments to ensure Nehemiah has ample time to process and respond to questions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Utilize test formats that include visual aids and simplify language to aid comprehension, reducing cognitive load during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Limit the number of items per page on written exams to avoid overwhelming him and to help maintain focus throughout the testing periods.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu'), 'Xzavier Smith''s Individual Education Program (IEP) is designed to address his needs under the category of Other Health Impairment, focusing on challenges associated with ADHD and chronic illnesses. Recognizing Xzavier''s need for structured support in managing his attention deficits, energy levels, and medical needs, the IEP includes goals and services that capitalize on his strengths and address his educational challenges. Specialized instruction focuses on cognitive-behavioral strategies and interventions that promote focus and engagement, particularly in his core academic subjects where he shows potential for improvement. Additionally, provisions for medication management and attendance flexibility are embedded within his daily school schedule to accommodate varying energy levels and medical appointments. Services such as counseling and health management support from the school nurse are also integral parts of his IEP to ensure a holistic approach to his educational and health needs.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Improve attention and task completion in academic tasks to a consistent 80% accuracy rate by incorporating behavior intervention plans and using positive reinforcement strategies.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Enhance reading and writing skills by 10% through differentiated instruction and the use of assistive technology tools designed to maintain engagement and improve comprehension.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Develop self-management skills in medication adherence and understanding of personal health needs through weekly sessions with the school nurse and monthly educational sessions on chronic illness management.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Provide extended time on district and statewide assessments (time and a half) to accommodate slower processing speeds associated with ADHD.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Allow for breaks every 30 minutes during testing to manage fatigue and attention fluctuations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Use of a quiet room for testing to minimize distractions and provide a controlled environment conducive to focusing.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu'), 'Destin Harris''s IEP is designed to support his educational progress with an emphasis on enhancing social skills, behavioral interventions, sensory processing, effective communication strategies, and the stabilization of routines. In terms of social skills, Destin will engage in structured group activities twice weekly, overseen by a special education teacher, aiming to improve his interaction and cooperation with peers. Behavioral interventions will include the consistent application of positive reinforcement techniques and a token economy to encourage appropriate behaviors, monitored and adapted monthly based on Destin''s progress. To assist with sensory processing, the classroom environment will be modified to minimize sensory overload, and Destin will have access to sensory tools such as noise-canceling headphones and fidget devices. Communication strategies will be bolstered through the use of visual supports and an augmentative communication device as needed, under the guidance of a speech and language therapist who will work with Destin twice a week. Routine stability will be addressed by implementing visual schedules and clear, consistent daily routines to reduce anxiety and improve Destin''s ability to transition between activities smoothly.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Increase ability to initiate and maintain age-appropriate conversations with peers and adults by 50% as measured by teacher observations and social skills checklist assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Demonstrate appropriate school behavior by reducing instances of disruptive behavior by 40% per semester as tracked through a behavior monitoring chart.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Utilize sensory tools effectively when experiencing sensory overload, with a decrease in sensory-related disruptions by at least 30%, as recorded by the special education team.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Improve expressive communication skills by increasing the use of multi-word phrases and augmentative communication devices in structured settings, aiming for a 35% improvement as measured by speech-language pathology assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Follow visual schedules independently for at least 90% of the school day, thereby reducing transition-related anxieties and interruptions as tracked by classroom teachers and aides.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Provide extended time for state and district-wide assessments, amounting to time and a half of the normal duration.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Administer tests in a small group setting to reduce distractions and provide a supported environment.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Use of an augmentative communication device during testing, if necessary, to better express understanding and responses.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Allow break periods as needed during assessments to manage sensory processing needs and reduce test-related anxiety.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu'), 'Cohen Munoz''s IEP is designed to support his specific learning disabilities, focusing on dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. Despite his exemplary grades, Cohen faces challenges with certain elements of reading and writing likely attributable to dyslexia. Our plan includes differentiated instruction in reading to enhance decoding skills, guided reading sessions to boost comprehension, and explicit instruction in math reasoning to develop problem-solving skills. Cohen will also participate in specialized writing workshops to strengthen his grammar and structure understanding, alongside strategic learning skills sessions to enable more effective information processing. His services will include weekly sessions with a reading specialist, bi-weekly math strategy workshops, and monthly consultations with a learning strategies advisor. Each session is data-driven, aiming to gauge Cohen''s progress through continuous assessments and adjust instructional strategies as needed.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Increase Cohen''s reading fluency and accuracy to grade-level expectations through specialized dyslexia interventions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Enhance Cohen''s reading comprehension to interpret and analyze texts more effectively, matching or exceeding grade-level benchmarks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Improve Cohen''s math reasoning skills to solve grade-level appropriate problems with increased precision and logic.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Advance Cohen''s writing skills by focusing on sentence structure, coherence, and organization to meet grade-level standards.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Develop Cohen''s adaptive learning strategies to support independent learning and information retention across all subject areas.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Provide extended time on all district and statewide assessments to ensure Cohen has adequate time to complete tasks without undue stress.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Offer test instructions both in written and oral formats to aid comprehension and ensure Cohen understands what is required in test settings.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Use of a word processor during writing assessments to help manage dyslexia-related challenges and allow Cohen to better structure his responses.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Allow breaks during testing and classwork to reduce cognitive fatigue and enhance overall performance.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Implementation of text-to-speech tools and audiobooks in standard testing and learning scenarios to support reading comprehension.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu'), 'Irene Barnes'' Individualized Education Program (IEP) is designed to address her academic needs resulting from her Other Health Impairment diagnosis, focusing specifically on ADHD, chronic illness management, and related challenges. In response to her needs, the IEP team has established a comprehensive plan that includes specialized instruction and tailored services intended to support Irene''s learning while managing her health-related needs effectively. To address her ADHD, Irene will receive targeted support through structured, small-group sessions with a special education teacher twice a week, emphasizing concentration strategies, coping mechanisms for distractions, and task completion skills. For chronic illness and medication management, Irene will receive routine check-ins with the school nurse to ensure proper medication adherence and to monitor potential side effects. Additionally, an attendance flexibility plan will be implemented to accommodate her varying energy levels and health condition, alongside modifications in physical education and other energy-intensive activities.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'To enhance Irene''s focus and engagement in academic tasks by employing behavioral strategies and organizational skills training tailored to her needs associated with ADHD.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'To maintain consistency in Irene''s medication adherence and monitor health status through bi-weekly sessions with the school nurse, ensuring minimal disruption to her academic performance.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'To improve Irene’s academic performance by at least one letter grade in all subjects by the end of the school year through personalized instruction, assignment adjustments, and test-taking strategies appropriate to her cognitive and health needs.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Extended time on all district and statewide assessments to ensure Irene has ample time to process and respond to test items, considering her difficulties with concentration and stamina.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Option to take frequent breaks during exams, which will help manage fatigue and maintain focus, especially during longer assessment periods.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Access to a quiet room or alternative testing location to minimize distractions, supporting better concentration and overall performance on tests.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu'), 'Curtis Pittman''s individual education program (IEP) is designed to address his specific learning disabilities, focusing on dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. Targeted objectives include improving his ability to decode written material, enhancing comprehension skills, strengthening math problem-solving abilities, developing coherent writing capabilities, and learning effective strategies for information processing. Curtis will receive specialized reading instruction incorporating multisensory techniques three times per week, math reasoning sessions twice per week with an emphasis on conceptual understanding, and writing workshops that focus on structure and grammar. He will also have access to a learning strategies instructor to assist with organization and study skills. Progress will be frequently monitored through a combination of teacher assessments, standardized tests, and portfolio reviews to ensure that Curtis is meeting the set educational goals.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Increase reading fluency and comprehension to grade level by end of the school year through structured, multisensory reading interventions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Improve math reasoning skills to reach a minimum of 80% accuracy on standardized assessments by participating in specialized math reasoning tutoring sessions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Enhance writing skills to effectively organize and clearly express ideas in written form, achieving at least a B grade in writing by the next semester.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Extended time (time and a half) on all district and statewide assessments to ensure Curtis has adequate time to process questions and formulate responses.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Access to text-to-speech software during exams and in class to support reading comprehension and reduce the strain of decoding difficulties.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Option to respond orally in testing situations where written expression is not being specifically assessed, to minimize the impact of writing difficulties.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu'), 'Joaquin Casey''s Individual Education Program (IEP) is designed to address his unique educational needs due to his classification under Other Health Impairment, particularly focusing on his ADHD and chronic illness management. To support Joaquin''s academic performance and overall wellbeing, the IEP includes specialized instructions tailored to enhance his engagement and learning efficacy, while managing his health needs effectively. Objectives include improving attention span, developing strategies for chronic illness management including medication adherence, and implementing flexible attendance policies to accommodate fluctuating energy levels. The educational team will collaborate with Joaquin to establish a consistent routine that includes regular check-ins and personalized support in organizing tasks and managing time effectively. Services such as counseling, occupational therapy, and access to a school nurse will be integral parts of his weekly schedule to ensure comprehensive support.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'Improve Joaquin''s academic performance in core subjects to a B average by providing individual tutoring sessions twice a week focusing on math and science comprehension strategies.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'Enhance Joaquin''s ability to manage his ADHD symptoms and regulatory focus through weekly sessions with the school psychologist, utilizing cognitive-behavioral techniques and behavior modification strategies.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'Establish and maintain effective chronic illness management routines, including medication adherence and energy management skills, to decrease school absences by 25% over the upcoming school year.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'Provide extended time on district and statewide assessments, allowing Joaquin 50% additional time to complete tests and assignments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'Allow for rest periods during school hours as needed to manage energy levels, particularly on days of prolonged academic activities or assessment.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'Use of a word processor for writing assignments and tests to support Joaquin in maintaining his focus and organizing his thoughts more effectively.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu'), 'Dean Madden, an 8th-grade student diagnosed with Specific Learning Disabilities, has an IEP tailored to address challenges in dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. The program comprises specialized instructional methods, including multi-sensory reading strategies, systematic and explicit instruction in math reasoning, and guided writing practices. Dean will receive differentiated reading instruction focused on improving phonemic awareness and decoding skills, pivotal for his dyslexia. In math, emphasis will be placed on developing his conceptual understanding and problem-solving abilities through hands-on activities and visual aids. For writing, specialized interventions will target organizational skills and coherence in writing structure. Additionally, Dean will participate in sessions with a learning strategies specialist, aiming to equip him with techniques to enhance his overall learning efficiency and classroom performance. Each area will incorporate formative assessments bi-weekly and a comprehensive review every quarter to monitor progress and adjust teaching strategies as needed.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Increase Dean''s reading fluency to grade level by utilizing targeted phonics instruction and continuous progress monitoring.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Enhance mathematical reasoning skills by 15% through the use of manipulatives, visual aids, and real-world problem-solving scenarios.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Improve writing skills to meet grade-level expectations, focusing on paragraph structure and clarity in expression. '),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Develop effective learning strategies that enable Dean to independently approach and accomplish classroom tasks and homework.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Provide extended time (time and a half) on all district and statewide assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Allow for the use of text-to-speech software during tests and class assignments to assist with reading comprehension.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Administer assessments in a distraction-reduced environment to improve focus and test-taking efficacy.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu'), 'Derrick Gibson''s IEP is designed to address his needs in the areas identified under his diagnosis of Specific Learning Disabilities, particularly focusing on dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. The program will include specialized instruction in reading and writing to enhance phonemic awareness and decoding skills through multisensory teaching methods. In math, Derrick will receive instruction focused on developing conceptual understanding and problem-solving abilities using visual aids and manipulatives. Weekly sessions with a special education teacher will aim to strengthen Derrick''s executive functioning skills, including organization and study techniques. Progress will be monitored bi-weekly through assessments conducted in a one-on-one setting to ensure personalized adjustments to the teaching methods.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'To increase Derrick''s reading comprehension level by at least two grade levels, utilizing targeted interventions that address specific deficits in phonemic awareness and decoding abilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'To improve Derrick''s math reasoning and problem-solving skills to meet grade-level standards, employing visual learning strategies and real-world application problems.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'To enhance Derrick''s writing ability to effectively communicate ideas, focusing on sentence structure, grammar, and clarity, increasing his writing scores by 15%.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'Extended time on all district and statewide assessments to ensure sufficient time to comprehend and respond to tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'Use of a word processor during writing tests to aid in organizing and expressing thoughts more clearly.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'Option to take tests in a small group setting to reduce anxiety and distraction.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu'), 'Crew King''s IEP is tailored to address his orthopedic impairments and ensure seamless access and participation in his academic environment. The primary focus areas include enhancing Crew''s mobility through the use of appropriate mobility aids, providing regular physical therapy sessions to improve his motor skills, and integrating adaptive equipment in the classroom to facilitate his learning process. Crew will receive specialized instruction that incorporates the use of technology and equipment designed to reduce physical barriers, particularly in subjects where manual dexterity is required. This bespoke educational plan involves collaborative efforts with physical therapists and occupational therapists to monitor and adjust approaches according to Crew''s progress and comfort level.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'To improve Crew''s mobility within the school environment, ensuring he can navigate between classes and access all necessary facilities with minimal assistance.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'To enhance Crew''s fine motor skills, enabling him to perform school tasks such as writing and manipulating small objects with increased ease and independence.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'To ensure Crew receives consistent physical therapy sessions twice a week to enhance his physical strength and endurance, supporting his active participation in school activities.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'Provide extended time on district and statewide assessments to accommodate physical limitations and prevent fatigue.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'Allow use of adaptive technology during tests, such as speech-to-text software and adjustable work stations, to enable him to complete assignments and exams without physical strain.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'Ensure that examination rooms are accessible by wheelchair or other mobility aids, and are equipped with ergonomic seating to support posture and reduce discomfort during assessments.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu'), 'Bo Smith''s IEP focuses on tailored objectives and interventions to enhance his educational outcomes, particularly in areas impacted by his specific learning disabilities. Despite high academic performance, challenges with dyslexia and reading comprehension require targeted support. For reading comprehension, structured literacy strategies will be integrated, emphasizing phonemic awareness and phonics, supported by bi-weekly sessions with a reading specialist. In math, Bo will engage in problem-solving workshops that focus on improving reasoning, offered weekly. Enhancing Bo’s writing skills will involve direct instruction in organization and syntax, with bi-weekly writing workshops. Across all subjects, Bo will utilize learning strategies that prioritize visual aids, mnemonic devices, and organizational tools to support memory and learning efficiency. Progress in these areas will be regularly monitored through formative assessments and reported in quarterly reviews to adapt strategies as necessary.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'To improve reading comprehension levels by one grade level by the end of the academic year through the use of structured literacy programs and consistent practice.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'To enhance math reasoning skills by integrating problem-solving strategies into weekly learning sessions and review their application in real-world scenarios.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'To develop writing skills by focusing on cohesive structuring and the use of comprehensive grammar aids, aiming for a 10% improvement in standardized writing assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'To implement and utilize advanced learning strategies that include visual aids and mnemonic techniques to aid in retention and application of learned material in all subjects.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Extended time on all district and statewide assessments, allowing time and a half on tests.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Provide test questions in both oral and written formats to accommodate learning preferences and to mitigate challenges with dyslexia.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Use of a word processor for written responses in state and district assessments to aid in organizing and structuring written responses.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Allowance for breaks every 30 minutes during assessments to reduce cognitive fatigue and maintain performance levels.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu'), 'Christian Nunez''s Individual Education Program (IEP) is designed to address his specific learning disabilities, particularly in the areas of dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. To support Christian''s literacy development, specialized instruction will focus on structured, multi-sensory reading interventions that are evidence-based for dyslexia. These will be implemented thrice weekly for 45-minute sessions. For math reasoning, Christian will receive targeted support in problem-solving and logical thinking, integrating visual and contextual learning aids during bi-weekly 40-minute sessions. Enhancing his writing skills, Christian will engage in direct instruction focusing on organization, clarity, and the mechanics of writing, with weekly sessions and ongoing feedback. Adaptive and strategic learning techniques tailored to his needs will be incorporated across subjects to improve his independent learning and study skills.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will improve his reading fluency and comprehension levels by 10% as measured by standardized reading assessments and curriculum-based measurements by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will demonstrate improved math problem-solving skills, achieving a 15% increase in accuracy on math reasoning tasks as evaluated through bi-monthly performance tasks and standardized tests.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will enhance his writing skills, showing progress in organization and clarity in written assignments, as measured by a writing rubric with targets set for every quarter.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Extended time on all district and statewide assessments, receiving time and a half to accommodate processing needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Access to text-to-speech software during reading and writing tasks in both classroom settings and standardized tests to support reading comprehension and written expression.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Permission to use a calculator during math assessments not measuring basic computation skills to support math reasoning.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu'), 'Robert Macdonald, an eighth-grade student diagnosed with Other Health Impaired, primarily characterised by ADHD and chronic illness, exhibits exceptional academic performance but requires specific supports to maintain this level. This IEP is designed to address Robert’s need for consistent medication management, tailored attendance flexibility, and effective energy management to cope with his symptoms during the school day. The plan includes specialized instructional strategies focusing on structured and supportive classroom environments and regular coordination with his healthcare team to monitor his health needs. Moreover, short, frequent breaks and a flexible scheduling option will be integrated to accommodate fluctuations in energy. This approach aims to ensure Robert''s continued academic success while managing his health effectively.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'To effectively manage ADHD symptoms and enhance focus in class through daily medication monitoring and bi-weekly counseling sessions with the school psychologist.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'To maintain an attendance rate of at least 90% by implementing flexible scheduling and virtual learning options on days when physical attendance is challenging due to health.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'To optimize energy levels throughout the school day via structured breaks every 90 minutes and by providing a rest area accessible for use during or between classes as needed.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'Provide extended time for tests and assignments, specifically accommodating slow processing speeds attributed to medication side effects or fatigue.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'Utilize technology-assisted learning tools for days of remote education to ensure continuity in learning when Robert is unable to attend school.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'Offer alternative, quiet testing locations to minimize distractions and manage anxiety during district and statewide assessments.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu'), 'Savanna Mahoney''s Individual Education Program (IEP) is designed to meet her unique needs as a student classified under Other Health Impairment, primarily due to ADHD and chronic illness. The IEP focuses on enhancing her academic performance and overall school experience through tailored strategies. Objectives include improving attention and focus in class, managing her health needs without disrupting her educational progress, and addressing her energy levels throughout the school day. Savanna will receive specialized instruction in all core subjects, with an emphasis on structured learning sessions to accommodate her concentration levels. Additionally, her IEP includes therapy sessions thrice weekly that focus on behavioral strategies for managing ADHD and counseling to support her emotional well-being, coping with chronic illness.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Improve Savanna''s attention span and participation in class through behavioral intervention plans and the use of adaptive technologies that aid learning.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Enhance academic performance in Math, Reading, Writing, Social Studies, and Science, aiming for a progress of at least 10% in grades by the next evaluation period.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Develop effective strategies for medication management and health monitoring during school hours, in collaboration with school nurses and her healthcare provider.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Provide extended time on tests and assignments to account for health-related absences and energy management issues.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Permit breaks during classes and examinations, as needed, to help manage fatigue and maintain concentration.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Utilize seating arrangements that minimize distractions and are close to necessary amenities such as the nurse''s office.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu'), 'Leighton Fisher''s IEP focuses on enhancing adaptive skills by incorporating behavioral interventions and social skills training sessions, conducted twice weekly, to foster better interpersonal interactions. The program aims to improve functional academics, especially in math and science, through the use of modified curricular content and hands-on learning activities adapted for her comprehension level. Emphasis on daily living activities includes structured task sequences and visual aids to support step-by-step learning, improving personal responsibility and self-care skills. Cognitive development will be engaged through problem-solving exercises and cognitive behavior techniques, aiming to increase Leighton''s ability to process and apply information effectively. Social development goals involve participation in peer-group activities under supervision to enhance her social interaction and understanding of social cues.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Increase Math and Science comprehension scores by 10% by the end of the school year through the use of specialized instructional strategies and resources.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Enhance adaptive behaviors by developing and following a plan that includes the use of social stories, role-playing, and peer interaction exercises, aiming for a reduction in social conflicts and increased peer relationship skills.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Improve daily living skills to a level where Leighton can follow multi-step procedures with minimal supervision, including managing personal care routines and organizational tasks.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Provide extended time for district and statewide assessments, allowing 50% additional time as compared to the time allotted to peers.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Utilize read-aloud accommodations for exam questions to support comprehension and processing difficulties.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Offer small-group testing environments to reduce stress and distractions, thereby optimizing test performance.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu'), 'Lisa Lewis''s Individualized Education Program (IEP) is designed to support her educational development under the category of Specific Learning Disabilities, with a focus on dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. She will receive specialized instruction in reading and writing, tailored to address her needs concerning dyslexia and to enhance her already strong performance. Strategies will include multisensory reading and phonetic instruction, aimed at improving decoding skills and reading fluency. In writing, targeted support will be provided to improve composition and structure, emphasizing clarity and organization. In math, Lisa will engage in reasoning exercises and problem-solving sessions to deepen her understanding of mathematical concepts and enhance application skills. Lisa will meet with a special education teacher thrice weekly for focused sessions and will have access to learning strategy workshops once a month to reinforce effective study habits and cognitive strategies.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'Improve decoding skills and reading fluency through structured multisensory reading sessions and systematic phonics instruction.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'Enhance writing skills by focusing on composition and structure, with specific objectives set to improve clarity and organization in written assignments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'Advance mathematical reasoning abilities through targeted problem-solving exercises and conceptual understanding in bi-weekly focused instruction sessions.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'Extended time on all district and statewide assessments to ensure thorough comprehension and response formulation.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'Access to a word processor during writing assessments to support organization and structure of essays.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'Provision of written and oral instructions for assessments to aid understanding and completion of tasks.');

COMMIT;


