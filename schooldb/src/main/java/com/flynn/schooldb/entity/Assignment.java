package com.flynn.schooldb.entity;

import jakarta.persistence.*;

import java.time.LocalDate;

@Entity
@Table(name="assignment")
public class Assignment {


    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "assignment_id")
    private Long assignmentId;

    @Column(name = "assignment_title", nullable = false)
    private String assignmentTitle;

    @Column(name = "assignment_type", nullable = false)
    private String assignmentType;

    @Column(name = "assignment_value", nullable = false)
    private Long assignmentValue;

    @Column(name = "date_assigned", nullable = false)
    private LocalDate dateAssigned;

    @Column(name = "date_due", nullable = false)
    private LocalDate dateDue;

    @ManyToOne
    @JoinColumn(name = "course_id", nullable = false)
    private Course course;

    public Assignment() {
    }

    public Assignment(Long assignmentId, String assignmentTitle, String assignmentType, Long assignmentValue, LocalDate dateAssigned, LocalDate dateDue, Course course) {
        this.assignmentId = assignmentId;
        this.assignmentTitle = assignmentTitle;
        this.assignmentType = assignmentType;
        this.assignmentValue = assignmentValue;
        this.dateAssigned = dateAssigned;
        this.dateDue = dateDue;
        this.course = course;
    }

    public Long getAssignmentId() {
        return assignmentId;
    }

    public void setAssignmentId(Long assignmentId) {
        this.assignmentId = assignmentId;
    }

    public String getAssignmentTitle() {
        return assignmentTitle;
    }

    public void setAssignmentTitle(String assignmentTitle) {
        this.assignmentTitle = assignmentTitle;
    }

    public String getAssignmentType() {
        return assignmentType;
    }

    public void setAssignmentType(String assignmentType) {
        this.assignmentType = assignmentType;
    }

    public Long getAssignmentValue() {
        return assignmentValue;
    }

    public void setAssignmentValue(Long assignmentValue) {
        this.assignmentValue = assignmentValue;
    }

    public LocalDate getDateAssigned() {
        return dateAssigned;
    }

    public void setDateAssigned(LocalDate dateAssigned) {
        this.dateAssigned = dateAssigned;
    }

    public LocalDate getDateDue() {
        return dateDue;
    }

    public void setDateDue(LocalDate dateDue) {
        this.dateDue = dateDue;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }
}
