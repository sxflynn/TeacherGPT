BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu'), 'Helen Moore''s Individual Education Program (IEP) is tailored to address her Specific Learning Disabilities focusing on Dyslexia, Reading comprehension, Math reasoning, Writing skills, and Learning strategies. Her objectives include improving decoding skills, enhancing reading fluency, mastering multi-step math problems, refining writing mechanics, and applying effective learning techniques. Helen will receive specialized instruction in a small group setting to support her educational goals and enhance her overall academic performance.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Helen will improve her decoding skills by correctly identifying and pronouncing words at her grade level with 90% accuracy by the end of the semester.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Helen will enhance her reading comprehension by summarizing and analyzing texts, answering inferential questions, and making connections to real-world scenarios with 85% accuracy by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Helen will demonstrate proficiency in solving multi-step math problems involving various operations, including addition, subtraction, multiplication, and division with 80% accuracy by the end of the academic year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Helen will refine her writing skills by incorporating proper grammar, punctuation, and sentence structure in her compositions, leading to coherent and organized written pieces with 85% accuracy by the end of the semester.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Helen will develop effective learning strategies by utilizing graphic organizers, mnemonic devices, and other tools to facilitate information retention and retrieval across subjects, showing improvement in self-regulation and study skills by the end of the school term.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'For district and statewide assessments, Helen will be provided with extended time to complete exams, allowing her to process information at her own pace and demonstrate her knowledge accurately.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Helen will have access to an electronic reader for exams to alleviate reading difficulties and ensure she comprehends questions effectively during testing.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'During assessments, Helen will be allowed to take breaks as needed to manage her focus and attention, promoting optimal performance and reducing test-related stress.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Instructions for assessments will be clearly written and verbally explained to Helen to address any potential reading comprehension challenges and ensure she fully understands the tasks and questions presented.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'hnmoore29@titanacademy.edu')), 'Helen will be permitted to use a word processor for writing tasks, enabling her to convey her thoughts fluently without being hindered by handwriting issues, to showcase her writing skills effectively on assessments.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu'), 'Damien Adams, diagnosed with Speech and Language disorder, requires targeted assistance in Articulation, Expressive and Receptive Language, Communication aids, and Speech therapy to enhance his communication skills. Through specialized instruction and services, Damien aims to improve his pronunciation, language expression, comprehension, and overall communication abilities.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'Damien will improve his articulation by correctly producing targeted speech sounds in words and sentences with 80% accuracy, as measured by monthly assessments conducted by the Speech-Language Pathologist.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'Damien will enhance his expressive language skills by using appropriate vocabulary and grammar in written and verbal communication, demonstrated by participating in class discussions and completing language exercises with 90% accuracy by the end of the semester.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'In receptive language, Damien will demonstrate comprehension of spoken and written instructions by following multi-step directions and summarizing information accurately in school tasks, achieving 85% accuracy in comprehension assessments quarterly.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'During district and statewide assessments, Damien will be provided with extended time to complete tasks, small group testing environments to minimize distractions, and access to a scribe or speech-to-text software for written responses.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'Additional accommodations include preferential seating near the teacher to facilitate understanding, visual aids such as graphic organizers or outlines for written tasks, and breaks as needed to manage attention and focus during testing sessions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ddadams29@titanacademy.edu')), 'Furthermore, Damien will have access to electronic devices for typing responses if needed and continued support from a paraprofessional for clarifying instructions and rephrasing questions to ensure comprehension and successful completion of assessment tasks.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu'), 'Lucy Mendoza''s IEP aims to enhance her social skills by fostering peer interaction and collaboration through structured group activities. Behavioral interventions will focus on promoting self-regulation techniques to manage emotions and reduce anxiety in various school settings. Sensory processing strategies will be implemented to support Lucy in sensory-rich environments and help her maintain focus during academic tasks. Communication strategies will prioritize developing her expressive language skills and comprehension abilities. Routine stability efforts will involve establishing consistent schedules and visual supports to minimize transitions and promote predictability in her daily school routine.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Lucy will initiate and maintain a conversation with a peer for at least 5 turns during structured social skills sessions, as measured by teacher observations twice a week.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Lucy will demonstrate self-calming techniques such as deep breathing or sensory tools when feeling overwhelmed, with goal mastery set at 80% accuracy during behavioral interventions conducted daily.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Lucy will participate in sensory breaks for proprioceptive input every 2 hours to support attention and engagement in academic tasks, to be monitored by the occupational therapist and teacher on a weekly basis.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'During district and statewide assessments, Lucy will be provided with a quiet testing environment and extended time based on her individual needs, as determined by the IEP team.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'Lucy will have access to a scribe or assistive technology for written responses on assessments to address any fine motor challenges that may impact her performance, as outlined in her accommodations plan.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lkmendoza29@titanacademy.edu')), 'To ensure fair assessment conditions, Lucy will receive directions broken down into simple steps and have the option for verbal clarification as needed during testing situations, with a testing specialist available to provide support.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu'), 'Irene Romero''s IEP aims to foster her social skills by encouraging peer interaction and joint activities. Behavioral interventions focus on self-regulation techniques to enhance classroom participation. Sensory processing strategies involve providing a sensory-friendly environment to mitigate sensory challenges. Communication strategies include implementing visual aids and augmentative communication tools. Routine stability will be supported through consistent schedules and visual schedules to promote predictability and reduce anxiety.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Irene will initiate and sustain interactions with peers during structured activities, with a goal of increasing social engagement by 25% within one semester.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Irene will independently utilize self-regulation techniques, such as deep breathing exercises, to manage emotional responses and maintain focus during academic tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Irene will demonstrate improved sensory processing by actively seeking and utilizing sensory tools to regulate her sensory input and decrease instances of sensory overload.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'During district and statewide assessments, Irene will be provided with extended time allowances to complete tasks and breaks as needed to regulate her sensory needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Assessments will be administered in a quiet, low-distraction environment to support Irene''s focus and attention during testing.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ihromero29@titanacademy.edu')), 'Irene will have access to a designated support staff member during assessments to provide verbal prompts or redirection as necessary to assist with task comprehension.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu'), 'Warren Perry''s Individual Education Program (IEP) outlines targeted objectives to support his development in adaptive skills, functional academics, daily living activities, social development, and cognitive abilities. The IEP aims to enhance Warren''s independence and academic success by providing specialized instruction and services tailored to his specific needs.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Warren will demonstrate improved adaptive skills by effectively utilizing resources and tools to enhance his learning experience and problem-solving abilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Warren will work on enhancing his functional academic skills by setting clear goals, using strategies to organize information, and independently completing academic tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Warren will develop daily living activities, such as personal hygiene routines, time management skills, and basic household tasks, to increase his self-sufficiency and independence.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Warren will focus on social development by participating in structured social skills activities, practicing effective communication, and fostering positive relationships with peers and adults.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Warren will engage in cognitive development activities to enhance his critical thinking skills, memory retention, and ability to process information across various academic subjects.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'For district and statewide assessments, Warren will receive extended time accommodations to ensure he can demonstrate his knowledge and skills without time pressure.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Warren will have access to a quiet, distraction-free environment during assessments to optimize his focus and concentration while completing tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'wcperry29@titanacademy.edu')), 'Additionally, Warren will be allowed the use of assistive technology tools, such as text-to-speech software or word prediction programs, to facilitate his understanding and expression of ideas during assessments.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu'), 'Arnav Williams, a sixth-grade student with Specific Learning Disabilities in Dyslexia, is working towards improving his reading comprehension, math reasoning, writing skills, and learning strategies. His IEP focuses on individualized instruction and support to address his academic challenges and promote growth in these key areas. Specialized interventions tailored to his needs will be provided to enhance his learning experience and help him achieve his educational objectives.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Arnav will improve his reading comprehension skills by implementing strategies such as graphic organizers and summarization techniques. Progress will be measured through bi-monthly reading assessments and teacher observation.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Arnav will enhance his math reasoning abilities by engaging in hands-on activities, visual aids, and personalized practice sessions. Progress monitoring will include weekly math quizzes and periodic evaluations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Arnav will develop stronger writing skills by utilizing sentence structure exercises, peer editing, and creative prompts. Improvement will be tracked through monthly writing samples and teacher feedback.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Arnav will enhance his learning strategies by employing techniques such as time management tools, note-taking skills, and self-assessment practices. Progress will be documented through regular check-ins and self-reflection exercises.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Arnav will be provided extended time for completing tests and assignments to accommodate his processing speed challenges.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'Arnav will receive preferential seating near the teacher to minimize distractions and promote focus during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'acwilliams29@titanacademy.edu')), 'During district and statewide assessments, Arnav will have access to a scribe or speech-to-text technology for written portions to assist with his dyslexia and writing difficulties.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu'), 'Braelyn Bauer''s IEP focuses on enhancing social skills, behavioral interventions, sensory processing, communication strategies, and routine stability. To achieve these goals, specialized instruction and services will be provided to support Braelyn in reaching her educational milestones and thriving in the school environment.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Braelyn will improve her social skills by engaging in structured group activities twice a week, where she will practice turn-taking, initiating conversations, and maintaining eye contact.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Braelyn will work on behavioral interventions by using a visual schedule and a reward system to encourage positive behaviors, reduce instances of meltdowns, and enhance self-regulation strategies.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Braelyn will receive sensory processing support through individualized sensory breaks incorporated into her daily routine, allowing her to self-regulate and remain focused during academic tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Braelyn will enhance her communication strategies by participating in weekly speech therapy sessions focusing on expressive language and social communication skills.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Braelyn''s routine stability will be supported by maintaining a consistent daily schedule and providing advance notice of any changes, ensuring predictability and lowering anxiety levels.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'For district and statewide assessments, Braelyn will be provided with a quiet room for testing to minimize distractions and sensory overload, along with extended time as needed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Accommodations will also include having a designated aide present during assessments for redirection and clarification, ensuring Braelyn comprehends instructions and tasks effectively.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcbauer29@titanacademy.edu')), 'Assessment progress will be measured through individualized checklists, rubrics, and teacher observations, with ongoing communication between school staff, parents, and Braelyn''s support team to monitor and adjust accommodations as necessary.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu'), 'Quentin Brown''s IEP is tailored to address his challenges in Dyslexia, Reading comprehension, Math reasoning, Writing skills, and Learning strategies. The core objectives are to improve Quentin''s decoding skills, enhance reading fluency and comprehension, develop problem-solving strategies in math, refine his written expression, and implement effective learning techniques.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Quentin will demonstrate a 15% improvement in decoding skills by the end of the school year, as measured by pre and post-assessments conducted bi-monthly.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Quentin will increase his reading comprehension accuracy by 20% through the use of graphic organizers and reading strategies, assessed through weekly comprehension quizzes.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Quentin will enhance his math reasoning abilities by mastering multi-step word problems with 80% accuracy by the conclusion of the semester.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Quentin will receive extended time accommodations for district and statewide assessments, allowing 1.5 times the standard testing duration.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Quentin will have access to audiobooks and text-to-speech software during reading and writing tasks to support his comprehension and written expression.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'qpbrown29@titanacademy.edu')), 'Quentin will be provided with preferential seating in the classroom to minimize distractions and aid his focus during instruction and assessments.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu'), 'Arthur Kelley''s individual education program (IEP) aims to support his specific learning disabilities in dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. To aid in his progress, Arthur will receive specialized instruction tailored to his needs in each of these areas, with a focus on developing foundational skills and implementing effective learning strategies.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'By the end of the semester, Arthur will improve his reading comprehension skills by identifying main ideas, supporting details, and making inferences with 80% accuracy in classroom assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'Arthur will enhance his math reasoning abilities by solving multi-step word problems involving all four operations with 85% accuracy, as measured by bi-weekly assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'Within the next academic year, Arthur will develop his writing skills, including organization, coherence, and grammar, resulting in compositions that convey ideas clearly and cohesively.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'During district and statewide assessments, Arthur will be provided extended time to complete tasks to alleviate time pressure and allow for thorough responses.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'Arthur will have access to a quiet room for testing to minimize distractions and optimize his focus during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'aakelley29@titanacademy.edu')), 'For written assignments and tests, Arthur will utilize assistive technology tools such as text-to-speech software to support his reading and writing needs.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu'), 'Clare Clark, a 6th-grade student with a diagnosis of Speech And Language impairment, will focus on improving articulation, expressive language, receptive language, and utilizing communication aids through specialized instruction. Clare will receive individualized speech therapy sessions twice a week to address these areas, with progress tracked through regular assessments and performance monitoring.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Clare will improve articulation by producing clear speech sounds in isolation and within words at 90% accuracy by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Clare will enhance expressive language skills by using appropriate vocabulary and sentence structures to express thoughts and ideas independently in 80% of opportunities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Clare will strengthen receptive language by following multi-step directions and comprehending complex texts at grade level with 85% accuracy by the end of the semester.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'During district and statewide assessments, Clare will be provided with extended time to process and respond to questions to demonstrate her knowledge effectively.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'Clare will have access to visual supports such as graphic organizers and word banks to aid in understanding test instructions and prompts.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cyclark29@titanacademy.edu')), 'For written assignments, Clare will be allowed to use speech-to-text software to assist in generating written responses accurately and efficiently.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu'), 'Allan Gibson, a sixth-grade student diagnosed with Speech and Language needs, will be focusing on improving his articulation, expressive and receptive language skills, and utilizing communication aids with targeted speech therapy services. Specialized instruction will be provided to enhance Allan''s communication abilities and overall language development.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will increase his articulation accuracy by 15% over the course of the school year through speech therapy sessions twice a week, as measured by a speech-language pathologist using standardized articulation assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will improve expressive language skills by expanding his vocabulary and sentence structure, participating in weekly language enrichment activities in small group settings, with progress tracked using expressive language assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will enhance receptive language by improving understanding of spoken language, engaging in receptive language tasks in the classroom daily, with a focus on following multi-step directions and comprehending complex sentences, monitored through teacher observations and receptive language assessments.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will be provided with extended time accommodations for district and statewide assessments to alleviate time pressure and allow for a more relaxed testing environment, enabling him to demonstrate his true abilities without time constraints.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will have access to a quiet testing environment with minimal distractions during assessments to support his focus and concentration, ensuring that external factors do not interfere with his performance on tests.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'algibson29@titanacademy.edu')), 'Allan will receive preferential seating during assessments to minimize auditory and visual distractions, allowing him to better attend to the test content and instructions, enhancing his overall test-taking experience.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu'), 'Millie Galvan''s IEP aims to enhance her articulation, expressive language, receptive language, and communication skills through targeted interventions. Specialized instruction and speech therapy sessions will focus on improving her ability to pronounce sounds accurately, express herself clearly, and comprehend language effectively. Communication aids will be utilized to support her in daily interactions and academic tasks.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'By the end of the school year, Millie will increase her articulation accuracy by 10%, as measured by a standardized speech assessment conducted quarterly.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'Millie will improve her expressive language skills by using at least five new vocabulary words per week in both spoken and written communication, as observed by her speech therapist during bi-weekly sessions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'Millie will enhance her receptive language abilities by accurately following multistep instructions in the classroom setting with 80% accuracy, as documented by her teachers through weekly progress reports.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'During district and statewide assessments, Millie will be provided with extended time to process and respond to test questions to accommodate her speech and language challenges.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'She will also have access to a quiet testing environment to minimize distractions that may hinder her concentration and performance during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mjgalvan29@titanacademy.edu')), 'For written portions, Millie will be allowed to use a word-to-text device to facilitate her responses, ensuring her knowledge and understanding are accurately captured in the evaluation.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu'), 'Cristopher Lowery''s IEP focuses on enhancing his social skills, behavioral interventions, sensory processing, communication strategies, and routine stability. The goals are aimed at fostering his ability to engage with peers, regulate behaviors, manage sensory input, communicate effectively, and adapt well to changes in routine. Specialized instruction will include social skills training, behavior management techniques, sensory tools, communication support, and structured routines to promote his overall development and success in the academic environment.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Cristopher will improve his social skills by initiating interactions with peers at least once per day and participating in group activities with minimal adult prompting.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Cristopher will demonstrate improved behavioral self-regulation by utilizing a provided visual schedule and practicing calming strategies when feeling overwhelmed, reducing disruptive incidents by 50% within the next grading period.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Cristopher will enhance his sensory processing abilities by engaging in daily sensory breaks and utilizing sensory tools to improve focus and attention during academic tasks.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'During district and statewide assessments, Cristopher will be provided with extended time as needed to complete tasks and breaks to manage sensory needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'He will have access to a quiet, designated testing area to minimize distractions and will be allowed the use of preferred sensory tools, such as fidget toys, to support focus during testing.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'celowery28@titanacademy.edu')), 'Instructions for assessments will be given in a clear and structured manner, and he will have the option of oral presentation for written responses to demonstrate his knowledge effectively.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu'), 'Jeremiah Robinson''s IEP aims to enhance his cognitive functioning, memory retention, physical abilities, neurological assessment outcomes, and behavioral responses. Through individualized instruction and targeted therapies, he will work towards improving his executive functions, memory consolidation, motor skills, neurological communication, and behavioral self-regulation.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will demonstrate improved cognitive processing by utilizing personalized cognitive rehabilitation strategies to enhance attention, problem-solving, and critical thinking skills in academic tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will utilize memory aids such as visual cues, reminders, and organizational tools to enhance his memory retention and recall across various subjects and daily activities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will participate in physical therapy sessions twice a week to improve his strength, coordination, balance, and fine motor skills to support his overall physical development and classroom engagement.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will undergo regular neurological assessments every six months to monitor and evaluate his brain injury-related progress, identify potential areas for intervention, and adjust therapeutic strategies accordingly.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will engage in behavioral adaptations training to develop self-regulation strategies, emotional coping mechanisms, and social skills to foster positive interactions with peers and educators in diverse learning environments.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will be provided extended time accommodations during district and statewide assessments to compensate for processing speed challenges linked to his brain injury.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will have access to a quiet testing environment free of distractions to minimize potential triggers and optimize his focus during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will be allowed the use of assistive technology tools such as text-to-speech software or word prediction programs to support his expression of knowledge and understanding during testing.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will receive regular breaks during testing sessions to prevent cognitive fatigue and maintain his optimal performance levels throughout the assessment period.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jkrobinson28@titanacademy.edu')), 'Jeremiah will be offered the option of oral administration for test instructions and questions to ensure comprehension and reduce potential barriers related to written directions.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu'), 'Nathalie Coleman''s IEP focuses on enhancing her social skills, behavioral interventions, sensory processing, communication strategies, and routine stability to support her academic and personal growth. Through individualized interventions and specialized services, Nathalie will work towards improving her interactions with peers, managing behavioral challenges, regulating sensory input, enhancing communication abilities, and establishing stable routines for increased independence and success.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Nathalie will demonstrate improved social skills by engaging in structured social activities with peers for at least 15 minutes daily, showing progress in initiating conversations and sharing activities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Nathalie will develop effective communication strategies by participating in weekly speech therapy sessions focusing on expressive and receptive language skills, with the goal of enhancing verbal and nonverbal communication in various contexts.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Nathalie will enhance sensory processing by engaging in sensory breaks throughout the school day as needed, incorporating sensory tools and techniques to improve attention and self-regulation.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Nathalie will be provided with extended time and a quiet space for district and statewide assessments to minimize sensory distractions and support focused effort during testing.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Nathalie will have access to a scribe or assistive technology for written tasks during assessments as needed, ensuring that her performance reflects her understanding and knowledge without being hindered by fine motor challenges.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nkcoleman28@titanacademy.edu')), 'Nathalie will receive visual supports and preferential seating arrangements during assessments to aid in maintaining attention and following instructions effectively.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu'), 'Yadiel Marsh''s Individual Education Program (IEP) focuses on enhancing his skills in dyslexia, reading comprehension, math reasoning, writing, and learning strategies. With targeted efforts in these areas, Yadiel aims to strengthen his academic performance and overall learning experience. Specialized instruction and support services will be provided to help him meet his educational objectives.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Yadiel will improve his reading comprehension by increasing his ability to analyze and interpret texts across various subjects, demonstrating progress through assessments and reading logs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Yadiel will enhance his math reasoning skills by applying problem-solving strategies, accurately interpreting mathematical concepts, and independently solving complex math problems.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Yadiel will develop his writing skills by organizing ideas cohesively, improving grammar and syntax, and expressing himself effectively through written communication.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Yadiel will enhance his learning strategies by practicing effective note-taking techniques, time management skills, and seeking clarification when encountering academic challenges.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'During district and statewide assessments, Yadiel will be provided with extended time to complete tests, ensuring he has sufficient time to demonstrate his knowledge and skills.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Yadiel will have access to a quiet testing environment to minimize distractions and support his focus during assessments, enabling him to perform to the best of his abilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'For written assignments, Yadiel will be allowed to use assistive technology such as speech-to-text software to facilitate the writing process and enhance his productivity.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'yamarsh28@titanacademy.edu')), 'Yadiel will receive preferential seating in the classroom to optimize his participation and engagement in lessons, enhancing his learning experience and academic performance.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu'), 'Raul Salazar''s IEP focuses on enhancing his social skills, behavioral interventions, sensory processing, communication strategies, and routine stability. Through personalized intervention, Raul aims to improve his social interactions, manage behaviors effectively, regulate sensory input, communicate more clearly, and establish a predictable routine to support his learning.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Raul will participate in social skills training twice a week, targeting peer interaction and reciprocal communication.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Raul will engage in behavioral interventions with a behavior therapist once a week to develop coping strategies and emotional regulation.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Raul will work with an occupational therapist to address sensory processing challenges three times a week, focusing on sensory diet implementation and sensory integration techniques.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Raul will receive speech therapy twice a week to enhance his verbal and non-verbal communication skills in different contexts.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Raul will have a structured routine implemented throughout his day, including visual schedules and transition strategies, to provide stability and predictability.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Raul will be provided with extended time for district and state assessments to accommodate for processing delays and sensory sensitivities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Raul will have access to a quiet and calming environment during assessments to minimize distractions and promote focus.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Assessments will be administered in smaller group settings to reduce potential anxiety triggers for Raul.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'rmsalazar28@titanacademy.edu')), 'Instructions for assessments will be presented in both visual and auditory formats to best support Raul''s comprehension and communication needs.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu'), 'Jorge Morales''s IEP focuses on enhancing his tactile communication methods, braille proficiency, orientation and mobility skills, utilization of assistive technologies, and combined sensory strategies. Specialized instruction includes hands-on learning experiences, braille literacy sessions, mobility practice, technology integration, and multisensory activities to promote holistic development.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'By the end of the school year, Jorge will demonstrate improved tactile discrimination and communication skills, as evidenced by correctly identifying various textures and shapes through touch.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'Jorge will enhance his Braille proficiency over the course of the year, reading and writing simple sentences independently with increasing accuracy and speed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'Within six months, Jorge will independently navigate familiar and unfamiliar environments using mobility aids, following specific routes with diminished assistance and increased confidence.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'During district and statewide assessments, Jorge will be provided with tactile graphics and braille versions of test materials as per his individual needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'Jorge will receive extended time on assessments to compensate for processing delays related to his dual sensory impairment.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jfmorales28@titanacademy.edu')), 'To facilitate effective communication during assessments, Jorge will be allowed to use assistive technologies such as screen readers and magnification software as outlined in his IEP.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu'), 'Edison Wyatt, a 7th-grade student with Orthopedic Impairments, will focus on enhancing physical accessibility, mobility aids utilization, physical therapy, adaptive equipment implementation, and motor skills development. The IEP aims to improve his overall motor function and independence, ensuring he can navigate the school environment comfortably while participating in academic and social activities. Specialized instruction and services will be personalized to support his specific needs in these areas, promoting a holistic approach to his educational progress.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'Edison will increase his independent mobility within the school setting by walking short distances without assistance at least 80% of the time.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'Edison will demonstrate improved fine motor skills by independently using adaptive equipment, such as a modified pencil grip, to complete writing assignments with 90% accuracy by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'Edison will participate in physical therapy sessions twice a week to strengthen core muscles and improve balance, aiming to enhance his overall physical capabilities for daily tasks.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'During district and statewide assessments, Edison will be provided with a separate quiet testing environment to minimize distractions and reduce sensory overload that may impact his performance.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'Edison will be allotted extra time on assessments, allowing him to work at his own pace without feeling rushed or pressured, ensuring he can fully demonstrate his knowledge and skills.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eawyatt28@titanacademy.edu')), 'Accommodations such as enlarged print materials and assistive technology devices will be provided to Edison as needed, catering to his visual and physical accessibility requirements during testing scenarios.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu'), 'Sadie Bennett''s IEP aims to enhance her educational experience through specialized instruction and services tailored to her visual impairment. Emphasis is placed on developing skills in Braille, utilizing visual aids effectively, enhancing orientation and mobility, utilizing low vision aids, and ensuring access to accessible materials to support her academic growth.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Sadie will improve her proficiency in reading Braille by correctly identifying and interpreting contracted and uncontracted Braille characters with 90% accuracy by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Sadie will effectively utilize visual aids, such as magnifiers and screen readers, to access and comprehend visual information in at least 80% of classroom activities by the end of each academic quarter.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Sadie will enhance her orientation and mobility skills by independently navigating different school environments, including classrooms, hallways, and common areas, with at least 95% accuracy by the end of the semester.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'During district and statewide assessments, Sadie will be provided with extended time as needed to complete tasks, with breaks to rest her eyes and maintain focus.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'Sadie will have access to a scribe or assistive technology to record her responses during assessments to ensure accurate transcription of her answers.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'stbennett28@titanacademy.edu')), 'All assessment materials will be made available in accessible formats, such as Braille or enlarged print, to facilitate Sadie''s active participation in the evaluation process.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu'), 'Sage Lyons'' IEP focuses on enhancing his social interaction, emotional regulation, and behavioral goals. Through specialized counseling services and targeted interventions, Sage aims to improve his coping mechanisms and self-awareness. The IEP includes a crisis plan to address potential challenges effectively.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Sage will demonstrate improved social skills by engaging in structured social activities with peers at least twice a week.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Sage will enhance his emotional regulation by utilizing mindfulness techniques during stressful situations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Sage will work on developing positive coping strategies to manage his emotions and reduce disruptive behaviors in the classroom.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'For district and statewide assessments, Sage will be provided extended time to complete tasks to account for processing delays.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Sage will have access to a quiet or alternative testing environment to minimize distractions during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sclyons28@titanacademy.edu')), 'Accommodations will include having questions read aloud to Sage to support his comprehension and ensure equitable assessment conditions.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu'), 'Mariyah Martinez''s individual education program (IEP) focuses on enhancing her skills in Dyslexia, Reading comprehension, Math reasoning, Writing skills, and Learning strategies. The specialized instruction and services to support Mariyah''s educational goals include targeted interventions in decoding strategies, comprehension techniques, problem-solving in math, fostering creative writing, and developing personalized learning strategies.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'Mariyah will increase her reading fluency and accuracy in decoding by 15% over the next academic year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'Mariyah will demonstrate improved reading comprehension by summarizing and analyzing grade-level texts independently with 80% accuracy by the end of the semester.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'Mariyah will enhance her math reasoning skills by solving multi-step word problems with at least 85% accuracy by the end of the year.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'For district and statewide assessments, Mariyah will be provided with extended time options to ensure she can demonstrate her knowledge effectively.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'Mariyah will also have access to audiobooks and text-to-speech tools to support her reading comprehension during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'mcmartinez28@titanacademy.edu')), 'During assessments, Mariyah will be allowed to use a word processor for written responses to accommodate her challenges in handwriting, ensuring her thoughts are clearly communicated.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu'), 'Elle Maddox''s IEP aims to enhance her skills in dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. The targeted progress includes improving reading fluency, math problem-solving, writing coherence, and implementing effective study strategies. Elle will receive specialized instruction tailored to her specific learning disabilities to support her in achieving these educational milestones.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Elle will improve her reading speed and accuracy by increasing her reading fluency level to reach grade-level expectations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Elle will enhance her math reasoning skills by independently solving multi-step word problems that involve multiple mathematical operations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Elle will strengthen her writing skills by organizing her ideas cohesively, using appropriate grammar and vocabulary to convey her thoughts effectively.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Elle will develop effective learning strategies to improve her study habits, including time management, note-taking, and test preparation techniques.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Elle will be provided extended time on district and statewide assessments to alleviate time pressure and enable her to demonstrate her true understanding of the material.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Elle will have access to audiobooks or text-to-speech tools for reading assignments to support her in comprehending the content effectively.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Elle will receive preferential seating in the classroom to minimize distractions and facilitate her focus during lessons and assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'eamaddox28@titanacademy.edu')), 'Elle will be granted the use of graphic organizers or outlines to assist in structuring her writing projects and organizing her thoughts coherently.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu'), 'Izaiah Mills'' Individual Education Program (IEP) aims to enhance his skills in Dyslexia, Reading comprehension, Math reasoning, Writing skills, and Learning strategies. To address Dyslexia, Izaiah will work on decoding strategies, fluency, and phonetic awareness. For Reading comprehension, he will focus on extracting main ideas, summarizing texts, and making inferences. In Math reasoning, he will practice problem-solving, mathematical fluency, and understanding abstract concepts. Regarding Writing skills, he will improve sentence structure, grammar, and organization. To enhance Learning strategies, Izaiah will develop note-taking skills, study habits, and time management techniques.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Izaiah will improve his decoding skills by accurately reading grade-level texts with minimal errors in phonetic sound recognition.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Izaiah will enhance his reading comprehension by accurately summarizing texts, identifying main ideas, and making inferences with 80% accuracy.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Izaiah will demonstrate improved math reasoning by correctly solving multi-step word problems and explaining his reasoning using mathematical language and concepts.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Extended time for completing assignments, especially reading and written tasks, to accommodate processing speed challenges.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Use of assistive technology such as text-to-speech software or spell-check applications to support writing assignments and assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ibmills28@titanacademy.edu')), 'Provision of a quiet and structured environment for testing, with breaks if needed, to minimize distractions during district and statewide assessments.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu'), 'Nehemiah Glover''s Individual Education Program (IEP) focuses on enhancing his adaptive skills, functional academics, daily living activities, social development, and cognitive development. Nehemiah will receive specialized instruction and support to help him progress in these areas, building on his strengths and addressing his needs comprehensively.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Nehemiah will improve his adaptive skills by independently completing personal care routines, such as grooming and dressing, with visual schedules and verbal prompts provided as needed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Nehemiah will enhance his functional academic abilities by increasing his proficiency in mathematical problem-solving and reading comprehension through interactive, hands-on activities tailored to his learning style.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Nehemiah will develop his daily living activities skills by learning and practicing tasks such as meal preparation, money management, and time management, with step-by-step guidance and opportunities for real-world application.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Nehemiah will work on social development by participating in structured social skills training sessions focusing on initiating conversations, interpreting social cues, and developing peer relationships in small group settings.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Nehemiah will strengthen his cognitive abilities by engaging in activities that promote critical thinking, decision-making, and problem-solving across various academic subjects, building his independence and confidence in learning.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'For district and statewide assessments, Nehemiah will be provided extended time to complete tasks, small group testing settings, and preferential seating to minimize distractions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'Nehemiah will also have access to assistive technology tools such as text-to-speech software and graphic organizers to support his comprehension and expression during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'nmglover28@titanacademy.edu')), 'To monitor Nehemiah''s progress, his assessments will include both qualitative and quantitative data collection methods, including teacher observations, work samples, and periodic meetings to review and adjust his IEP goals as needed.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu'), 'Xzavier Smith''s IEP aims to support his needs in managing ADHD symptoms, chronic illnesses, medications, attendance flexibility, and energy levels. The objectives include improving focus and organization skills, managing health conditions effectively, adhering to medication routines, ensuring attendance consistency, and optimizing energy for sustained participation in classroom activities. Through individualized support and services, Xzavier will work towards enhancing his academic performance and overall well-being.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Xzavier will demonstrate improved focus and task completion by engaging in organizational strategies such as utilizing visual schedules and breaking tasks into manageable steps.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Xzavier will effectively manage his chronic illnesses by adhering to medical protocols, communicating health needs to school staff, and engaging in self-care practices when necessary.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Xzavier will develop greater independence in medication management by following prescribed dosages, understanding medication purposes, and seeking help when needed.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Xzavier will be provided with preferential seating in the classroom to minimize distractions and enhance his focus during lessons and assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'Xzavier will have access to a quiet and designated space for breaks to manage his energy levels and recharge when feeling overwhelmed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'xksmith28@titanacademy.edu')), 'During district and statewide assessments, Xzavier will be allowed extended time accommodations, frequent breaks as needed, and access to a separate testing environment to ensure a conducive testing environment that aligns with his needs.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu'), 'Destin Harris''s Individual Education Program (IEP) is designed to support his progress in social skills, behavioral interventions, sensory processing, communication strategies, and routine stability. Through specialized instruction and services, Destin will work towards enhancing his social interactions, managing behaviors, improving sensory regulation, fostering effective communication, and establishing consistent routines to aid his learning.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Destin will develop social skills by engaging in structured peer interactions for at least 20 minutes daily, with progress measured through observation and social skills assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Destin will participate in behavioral interventions such as a token economy system to promote positive behaviors, with weekly reviews to assess response and effectiveness.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Destin will engage in sensory processing activities tailored to his needs, including sensory breaks as needed, with the goal of improving focus and regulation both at school and home.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Destin will have extended time and small-group setting accommodations for district and statewide assessments, ensuring a quiet environment and access to sensory tools like headphones if needed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'He will be allowed to use a word-to-word dictionary and have questions read aloud during assessments as per his accommodations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'drharris27@titanacademy.edu')), 'Destin''s assessments will be broken into smaller segments with built-in breaks as necessary to support his attention span and processing abilities.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu'), 'Cohen Munoz''s IEP is designed to support his specific learning disabilities in dyslexia, focusing on enhancing reading comprehension, math reasoning, writing skills, and learning strategies. Through personalized instruction and targeted interventions, Cohen will progress towards mastering essential academic skills and building confidence in his abilities.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Cohen will improve reading comprehension by utilizing decoding strategies and practicing summarizing texts to achieve grade-level proficiency.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Cohen will strengthen math reasoning skills through hands-on activities and visual aids, aiming to interpret and solve complex mathematical problems independently.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Cohen will enhance his writing skills by structuring coherent paragraphs, citing textual evidence, and refining grammar and punctuation for improved expression and coherence.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Cohen will develop effective learning strategies, such as time management techniques and study habits, to optimize his academic performance and promote independent learning.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Extended time on assessments to alleviate time pressure and allow Cohen to demonstrate his understanding without rushing.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Use of assistive technology tools, such as screen readers and speech-to-text software, to support writing assignments and reading tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Preferential seating in the classroom to minimize distractions and enhance Cohen''s focus during lessons and assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ckmunoz27@titanacademy.edu')), 'Access to a resource room for additional support and guidance, where Cohen can receive one-on-one assistance and clarification on challenging concepts.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu'), 'Irene Barnes, an eighth-grade student diagnosed with Other Health Impaired, will focus on enhancing her abilities in ADHD management, chronic illness awareness, medication self-regulation, attendance consistency, and energy allocation. To achieve these goals, Irene will receive personalized instruction and support services tailored to her needs in these areas to foster her academic and personal growth.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Irene will demonstrate improved attention and concentration skills by implementing structured strategies to manage her ADHD throughout the school day.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Irene will develop an understanding of her chronic illnesses, learning self-care techniques for symptom management, and advocating for her health needs.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Irene will enhance her ability to manage her medications independently, understanding dosages, schedules, and potential side effects to promote her overall well-being.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Irene will work towards maintaining regular attendance by utilizing a flexible attendance plan tailored to her needs, allowing for necessary accommodations when health challenges arise.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Irene will learn effective energy management techniques, pacing herself during academic tasks, and incorporating breaks as needed to optimize her learning potential.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'For district and statewide assessments, Irene will be provided extended time accommodations to complete tasks, ensuring she can demonstrate her full understanding and abilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Irene will have access to a quiet testing environment to minimize distractions during assessments, promoting her focus and concentration on the tasks at hand.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Irene will be allowed the use of preferential seating during assessments to support her comfort and attention, enabling her to perform to the best of her ability.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Irene will have the option of utilizing assistive technology tools during assessments, such as text-to-speech software, to aid in her comprehension and expression of ideas.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ikbarnes27@titanacademy.edu')), 'Irene will have the opportunity for frequent breaks during assessments as needed, enabling her to manage her energy levels and sustain focus throughout the testing period.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu'), 'Curtis Pittman''s IEP focuses on addressing his specific learning disabilities in dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. The goal is to enhance Curtis''s academic performance by providing targeted support in these areas.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Curtis will improve his reading comprehension by utilizing multisensory reading strategies. Progress will be measured through regular assessments to track growth and adjust interventions accordingly.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Curtis will enhance his math reasoning abilities through individualized instruction focusing on problem-solving skills and conceptual understanding. Ongoing monitoring will evaluate his progress and modify teaching strategies as needed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Curtis will develop his writing skills by practicing structured writing exercises that emphasize organization, grammar, and coherence. Assessments will be conducted to assess writing proficiency and guide instructional planning.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'During district and statewide assessments, Curtis will be provided extended time to complete tasks to accommodate his processing speed challenges.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'Curtis will have access to a quiet and distraction-free environment during testing to support his concentration and reduce sensory overload.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjpittman27@titanacademy.edu')), 'For written assessments, Curtis will be allowed to use assistive technology such as text-to-speech software to facilitate his responses and demonstrate his knowledge effectively.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu'), 'Joaquin Casey''s IEP focuses on addressing his needs in ADHD, chronic illnesses, medication management, attendance flexibility, and energy management. To support his progress, Joaquin will receive specialized instruction in organizational skills, task prioritization, and stress management. Services will include regular check-ins with a school counselor and targeted interventions to enhance his executive functioning abilities. The IEP aims to improve Joaquin''s ability to cope with stressors, adhere to a medication regimen, and optimize his energy levels for sustained engagement in academic tasks.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'Joaquin will demonstrate improved organizational skills by independently managing his school materials and assignments with 80% accuracy by the end of the semester.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'Joaquin will enhance his medication management by consistently adhering to his prescribed medication schedule over a 6-month period, as documented by weekly reports from the school nurse.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'Joaquin will develop strategies to effectively manage his energy levels by utilizing relaxation techniques and structured breaks to sustain focus during classroom activities, achieving this goal with 90% proficiency by the end of the school year.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'During district and statewide assessments, Joaquin will be provided with extended time accommodations to alleviate time pressure and allow for breaks as needed, supported by a designated staff member.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'For written assessments, Joaquin will be permitted to use a computer or assistive technology for typing to bypass potential challenges arising from his chronic illnesses affecting his handwriting speed, as recommended by an occupational therapist.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'jzcasey27@titanacademy.edu')), 'In cases of extended absences due to chronic illnesses, Joaquin will be granted flexible deadline accommodations for makeup assignments, ensuring fair assessment opportunities without compromising his health-related absences.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu'), 'Dean Madden''s IEP focuses on addressing his specific learning disabilities in dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. The IEP aims to enhance his academic performance through tailored interventions and support services to foster his growth and success in these critical areas.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Dean will improve his reading comprehension skills by utilizing multisensory approaches and strategies. Progress will be monitored through regular assessments to track his comprehension development.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Dean will enhance his math reasoning ability through targeted interventions and personalized instruction. His progress will be measured through problem-solving tasks and math assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Dean will boost his writing skills by practicing structured writing exercises and receiving feedback on organization and coherence. Improvement will be gauged through writing assignments and evaluations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Dean will develop effective learning strategies to improve his overall academic performance by engaging in study skills training, time management techniques, and organizational strategies. Progress will be assessed through self-monitoring and teacher observations.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'During district and statewide assessments, Dean will be provided extended time to complete tasks to ensure he can demonstrate his knowledge and skills effectively.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'Dean will have access to a quiet and distraction-free testing environment to minimize external stimuli that could impact his focus and concentration during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'demadden27@titanacademy.edu')), 'He will be allowed to use assistive technology tools such as text-to-speech software or graphic organizers as needed to support his comprehension and expression during testing situations.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu'), 'Derrick Gibson''s IEP focuses on enhancing his skills in Dyslexia, Reading comprehension, Math reasoning, Writing skills, and Learning strategies. Through targeted interventions, personalized instruction, and consistent support, Derrick aims to make significant progress in these key areas to reach his academic potential.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'By the end of the school year, Derrick will improve his reading fluency and accuracy, as measured by weekly assessments and teacher observations.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'Derrick will demonstrate an increase in math reasoning skills by successfully solving multi-step word problems and applying appropriate problem-solving strategies in daily math tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'In writing, Derrick will enhance his ability to organize ideas cohesively and expressively, as evidenced by improved essays and compositions that reflect structured content and clear communication.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'During district and statewide assessments, Derrick will be provided with extended time to complete tasks, as well as the option to have questions read aloud if needed.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'Derrick will have access to a quiet testing environment to minimize distractions and optimize his concentration during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'dagibson27@titanacademy.edu')), 'For written assignments, Derrick will be allowed the use of assistive technology tools such as speech-to-text software to facilitate the writing process and ensure his ideas are captured accurately.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu'), 'Crew King''s IEP aims to enhance his physical accessibility by ensuring a barrier-free environment within the school premises. Mobility aids will be provided to facilitate his movement, fostering a more independent lifestyle. Through regular physical therapy sessions and the utilization of adaptive equipment, Crew will work on improving his motor skills, aiding in his overall physical development.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'Crew will independently navigate the school environment, including ramps and doorways, with assistance only when necessary in 9 out of 10 opportunities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'By the end of the school year, Crew will demonstrate improved motor skills by independently using his mobility aid on different surfaces, with only occasional guidance from staff when transitioning between them.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'Crew will participate in physical therapy sessions twice a week to increase strength and coordination, as measured by regular progress assessments showing improvement in targeted areas.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'Crew will be provided with extended time and breaks during district and statewide assessments to accommodate his physical needs and ensure he can fully participate in the exams.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'For written components of assessments, Crew will be permitted to use a scribe when needed, allowing him to focus on conveying his knowledge without being hindered by his orthopedic condition.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cvking27@titanacademy.edu')), 'The school will implement frequent progress monitoring to track Crew''s development in motor skills and adjust the level of support and adaptive equipment provided based on his evolving needs and capabilities.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu'), 'Bo Smith, an eighth-grade student diagnosed with Specific Learning Disabilities, will receive specialized instruction to address his challenges in dyslexia, reading comprehension, math reasoning, writing skills, and learning strategies. The focus will be on fostering his academic growth through targeted interventions tailored to his needs, enabling him to excel in various subjects.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Bo will improve his reading comprehension by utilizing multi-sensory approaches and decoding strategies, aiming to increase his ability to extract and analyze information from texts independently.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Bo will enhance his math reasoning by engaging in hands-on activities and problem-solving tasks, with the goal of improving his critical thinking skills and numerical fluency.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Bo will develop his writing skills by practicing structured writing exercises, focusing on organization, coherence, and expression to enhance his communication abilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Bo will employ specific learning strategies such as graphic organizers and mnemonic devices to improve his memory retention, study habits, and overall academic performance.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'During district and statewide assessments, Bo will be provided extended time to complete tasks to ensure he has sufficient opportunity to demonstrate his knowledge and understanding.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Bo will have access to a quiet and distraction-free environment during assessments to optimize his focus and concentration on the tasks at hand.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'For written assignments and tests, Bo will be allowed to use assistive technology tools such as speech-to-text software or word prediction programs to support his written expression and composition.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'bcsmith27@titanacademy.edu')), 'Bo will receive frequent progress monitoring through regular check-ins with his teachers, adaptive assessments, and periodic reviews to assess his growth and adjust interventions accordingly.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu'), 'Christian Nunez''s IEP focuses on enhancing his skills in Dyslexia management, Reading comprehension, Math reasoning, Writing proficiency, and Learning strategies. Through personalized learning approaches, Christian will receive targeted instruction and interventions to support his academic development across these key areas.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will improve Dyslexia management by employing multisensory techniques to enhance phonemic awareness and reading fluency.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will enhance Reading comprehension by utilizing graphic organizers, summarization strategies, and vocabulary-building exercises.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will strengthen Math reasoning by engaging in problem-solving tasks, mathematical reasoning activities, and real-world application projects.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will advance Writing skills by practicing sentence structure, coherence, and incorporating descriptive language elements in his compositions.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will develop effective Learning strategies by fostering organization skills, time management techniques, and self-regulation strategies to support academic success.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will be provided additional time for district and statewide assessments to accommodate processing speed challenges.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will have the option for a separate, distraction-reduced environment during testing to ensure optimal focus and concentration.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will be granted the use of assistive technology tools such as speech-to-text software and text-to-speech resources for assessment tasks.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will receive individualized instructions for test-taking strategies to enhance his test performance and reduce test anxiety.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'cjnunez27@titanacademy.edu')), 'Christian will have access to a scribe or word processor for written portions of assessments to alleviate the impact of writing challenges on his responses.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu'), 'Robert Macdonald''s individual education program focuses on addressing his needs in managing ADHD, chronic illnesses, medication management, attendance flexibility, and energy levels. To support his progress in these areas, Robert will receive specialized instruction and services tailored to his needs, with an emphasis on creating a conducive learning environment.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'Robert will work towards improving his attention and focus in academic tasks by engaging in strategies such as frequent breaks and structured routines.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'Robert will develop skills to better manage his chronic illnesses by learning self-monitoring techniques and adhering to a personalized health plan.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'Robert will enhance his ability to manage medication effectively by utilizing visual aids and reminders to ensure consistency and timeliness.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'For district and statewide assessments, Robert will be provided extended time accommodations to mitigate the impact of his ADHD on test-taking abilities.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'Robert will have access to a quiet and low-stimulus testing environment to help him maintain focus during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'ramacdonald27@titanacademy.edu')), 'Additionally, Robert will be allowed to take breaks during the assessments as needed, with a designated staff member available to supervise and ensure a smooth testing experience.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu'), 'Savanna Mahoney''s IEP focuses on addressing her ADHD symptoms, chronic illnesses, medication management, attendance flexibility, and energy management to support her academic progress. Goals include improving attention span, managing symptoms effectively, ensuring consistent medication routines, accommodating flexible attendance options, and optimizing energy levels throughout the day. Specialized instruction and services will include individualized behavioral strategies, regular health monitoring, medication reminders, personalized attendance plans, and energy-conserving breaks to enhance learning experiences.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Savanna will demonstrate improved attention and focus in the classroom setting, as measured by sustained engagement in learning activities for at least 20 minutes without significant distraction.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Savanna will effectively manage her chronic illnesses, including symptom recognition and appropriate self-care strategies, with the aim of reducing health-related absences by 20% over the course of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Savanna will independently adhere to her medication schedule, self-administering prescribed medications at the designated times throughout the school day, ensuring optimal symptom management and minimal disruption to academic activities.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'For district and statewide assessments, Savanna will be provided with extended time options to complete tasks, ensuring that her performance reflects her knowledge and skills rather than time constraints.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'Savanna will have access to a quiet and distraction-free testing environment to minimize stimuli that could interfere with her concentration and performance during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'sdmahoney27@titanacademy.edu')), 'During assessments, Savanna may take short breaks as needed to manage her energy levels effectively, with a maximum of two breaks per assessment session, each lasting up to 5 minutes to reset and refocus.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu'), 'Leighton Fisher''s IEP focuses on enhancing her adaptive skills, functional academics, daily living activities, social development, and cognitive development. Targeted progress includes improving independent living skills, enhancing academic performance, refining self-care routines, fostering social interactions, and advancing cognitive abilities through individualized interventions. Specialized instruction and services such as personalized tutoring, occupational therapy, social skills training, and cognitive behavioral support will be provided to help Leighton achieve her educational objectives.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Leighton will independently complete basic daily living tasks, such as personal hygiene and household chores, with at least 80% accuracy by the end of the school year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Leighton will demonstrate an improvement of 10% in functional academics by utilizing personalized learning strategies and tools to achieve a B- grade level by the end of the semester.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Leighton will engage in social interactions with peers through structured activities and reciprocal conversations, demonstrating an increase in social skills and initiating interactions at least twice daily.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Leighton will receive extended time accommodations during district and statewide assessments to ensure she can demonstrate her knowledge and skills effectively.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Leighton will be provided with a quiet testing environment to minimize distractions and facilitate her concentration during assessments.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lrfisher27@titanacademy.edu')), 'Leighton will have access to a scribe or assistive technology for written portions of assessments to support her in conveying her responses accurately.');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO "iep" ("student_id", "iep_summary")
VALUES
((SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu'), 'Lisa Lewis''s Individualized Education Program (IEP) focuses on enhancing her skills in Dyslexia, Reading Comprehension, Math Reasoning, Writing Skills, and Learning Strategies. To support Lisa''s progress in these areas, specialized instruction and interventions tailored to her learning style and pace are implemented.');

INSERT INTO "iep_goals" ("iep_id", "goal")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'Lisa will improve her reading fluency and comprehension by utilizing phonics-based interventions, with a goal to enhance her reading level by one grade equivalent within the academic year.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'Lisa will enhance her math reasoning skills through multi-sensory instruction and problem-solving strategies, aiming to achieve proficiency in grade-level math concepts and applications.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'Lisa will develop her writing skills by practicing structured writing exercises and receiving direct feedback to improve organization, coherence, and mechanics.');

INSERT INTO "iep_accommodations" ("iep_id", "accommodation")
VALUES
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'For district and statewide assessments, Lisa will be provided extended time accommodations to ensure she can demonstrate her knowledge and skills without time constraints.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'During assessments, Lisa will have access to a quiet testing environment to minimize distractions and enable her to focus on the tasks at hand.'),
((SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = 'lelewis27@titanacademy.edu')), 'For written assignments and tests, Lisa will be allowed to use assistive technology tools, such as speech-to-text software or word prediction programs, to support her in expressing her knowledge effectively.');

COMMIT;

