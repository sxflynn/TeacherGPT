package com.flynn.schooldb.dto;

import com.flynn.schooldb.entity.Course;
import com.flynn.schooldb.entity.Student;

import java.time.LocalDate;
import java.util.Optional;

public class CourseGradeDTO {

    private Optional<Student> student;

    private Optional<Course> course;

    private LocalDate startDate;

    private LocalDate endDate;

    private Integer numberOfGradedAssignments;

    private Float averageScore;

    private String letterGrade;

    public CourseGradeDTO() {
    }

    public CourseGradeDTO(Optional<Student> student, Optional<Course> course, LocalDate startDate, LocalDate endDate, Integer numberOfGradedAssignments, Float averageScore, String letterGrade) {
        this.student = student;
        this.course = course;
        this.startDate = startDate;
        this.endDate = endDate;
        this.numberOfGradedAssignments = numberOfGradedAssignments;
        this.averageScore = averageScore;
        this.letterGrade = letterGrade;
    }

    public CourseGradeDTO(Optional<Course> course, LocalDate startDate, LocalDate endDate, Integer numberOfGradedAssignments, Float averageScore, String letterGrade) {
        this.course = course;
        this.startDate = startDate;
        this.endDate = endDate;
        this.numberOfGradedAssignments = numberOfGradedAssignments;
        this.averageScore = averageScore;
        this.letterGrade = letterGrade;
    }

    public Optional<Student> getStudent() {
        return student;
    }

    public void setStudent(Optional<Student> student) {
        this.student = student;
    }

    public Optional<Course> getCourse() {
        return course;
    }

    public void setCourse(Optional<Course> course) {
        this.course = course;
    }

    public LocalDate getStartDate() {
        return startDate;
    }

    public void setStartDate(LocalDate startDate) {
        this.startDate = startDate;
    }

    public LocalDate getEndDate() {
        return endDate;
    }

    public void setEndDate(LocalDate endDate) {
        this.endDate = endDate;
    }

    public String getAverageScore() {
        return String.format("%.2f%%", averageScore * 100);
    }

    public Integer getNumberOfGradedAssignments() {
        return numberOfGradedAssignments;
    }

    public void setNumberOfGradedAssignments(Integer numberOfGradedAssignments) {
        this.numberOfGradedAssignments = numberOfGradedAssignments;
    }

    public Float getAverageScoreFloat(){
        return this.averageScore;
    }

    public void setAverageScore(Float averageScore) {
        this.averageScore = averageScore;
    }

    public String getLetterGrade() {
        return letterGrade;
    }

    public void setLetterGrade(String letterGrade) {
        this.letterGrade = letterGrade;
    }
}
