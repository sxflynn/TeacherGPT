package com.flynn.schooldb.entity;

import jakarta.persistence.*;

import java.util.List;

@Entity
@Table(name="course")
public class Course {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="course_id")
    private Long courseId;

    @Column(name = "course_name", nullable = false)
    private String courseName;

    @ManyToOne
    @JoinColumn(name = "lead_teacher_id")
    private Staff leadTeacher;

    @ManyToOne
    @JoinColumn(name = "grade_level_id")
    private GradeLevel gradeLevel;

    @ManyToMany
    @JoinTable(
            name = "course_student",
            joinColumns = @JoinColumn(name = "course_id"),
            inverseJoinColumns = @JoinColumn(name = "student_id")
    )
    private List<Student> students;

}
