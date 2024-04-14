package com.flynn.schooldb.entity;

import jakarta.persistence.*;

@Entity
@IdClass(StudentScoreId.class)
@Table(name="student_score")
public class StudentScore {

    @Id
    @Column(name = "student_id")
    private Long studentId;

    @Id
    @Column(name = "assignment_id")
    private Long assignmentId;

    @Column(name = "points_earned")
    private Integer pointsEarned;

    @Column(name = "percentage_score")
    private Float percentageScore;

    @Column(name = "missing")
    private Boolean missing;

    @ManyToOne
    @JoinColumn(name = "student_id", insertable = false, updatable = false)
    private Student student;

    @ManyToOne
    @JoinColumn(name = "assignment_id", insertable = false, updatable = false)
    private Assignment assignment;

    public StudentScore() {
    }

    public StudentScore(Long studentId, Long assignmentId, Integer pointsEarned, Float percentageScore, Boolean missing, Student student, Assignment assignment) {
        this.studentId = studentId;
        this.assignmentId = assignmentId;
        this.pointsEarned = pointsEarned;
        this.percentageScore = percentageScore;
        this.missing = missing;
        this.student = student;
        this.assignment = assignment;
    }

    public Long getStudentId() {
        return studentId;
    }

    public void setStudentId(Long studentId) {
        this.studentId = studentId;
    }

    public Long getAssignmentId() {
        return assignmentId;
    }

    public void setAssignmentId(Long assignmentId) {
        this.assignmentId = assignmentId;
    }

    public Integer getPointsEarned() {
        return pointsEarned;
    }

    public void setPointsEarned(Integer pointsEarned) {
        this.pointsEarned = pointsEarned;
    }

    public String getPercentageScore() {
        return String.format("%d%%", Math.round(percentageScore * 100));
    }

    public void setPercentageScore(Float percentageScore) {
        this.percentageScore = percentageScore;
    }

    public Boolean getMissing() {
        return missing;
    }

    public void setMissing(Boolean missing) {
        this.missing = missing;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

    public Assignment getAssignment() {
        return assignment;
    }

    public void setAssignment(Assignment assignment) {
        this.assignment = assignment;
    }
}
