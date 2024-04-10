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

    @OneToMany(mappedBy = "course", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Assignment> assignments;

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

    public Course() {
    }

    public Course(Long courseId, String courseName, Staff leadTeacher, GradeLevel gradeLevel) {
        this.courseId = courseId;
        this.courseName = courseName;
        this.leadTeacher = leadTeacher;
        this.gradeLevel = gradeLevel;
    }

    public Long getCourseId() {
        return courseId;
    }

    public void setCourseId(Long courseId) {
        this.courseId = courseId;
    }

    public String getCourseName() {
        return courseName;
    }

    public void setCourseName(String courseName) {
        this.courseName = courseName;
    }

    public Staff getLeadTeacher() {
        return leadTeacher;
    }

    public void setLeadTeacher(Staff leadTeacher) {
        this.leadTeacher = leadTeacher;
    }

    public GradeLevel getGradeLevel() {
        return gradeLevel;
    }

    public void setGradeLevel(GradeLevel gradeLevel) {
        this.gradeLevel = gradeLevel;
    }
}
