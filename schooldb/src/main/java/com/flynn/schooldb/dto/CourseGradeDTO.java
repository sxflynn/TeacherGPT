package com.flynn.schooldb.dto;

import java.time.LocalDate;

public class CourseGradeDTO {

    private Long studentId;

    private String teacherLastName;

    private String courseName;

    private LocalDate startDate;

    private LocalDate endDate;

    private Integer numberOfGradedAssignments;

    private Float averageScore;

    private String letterGrade;

    public CourseGradeDTO() {
    }

    public CourseGradeDTO(Long studentId, String courseName, LocalDate startDate, LocalDate endDate, Integer numberOfGradedAssignments, Float averageScore, String letterGrade) {
        this.studentId = studentId;
        this.courseName = courseName;
        this.startDate = startDate;
        this.endDate = endDate;
        this.numberOfGradedAssignments = numberOfGradedAssignments;
        this.averageScore = averageScore;
        this.letterGrade = letterGrade;
    }

    public CourseGradeDTO(String teacherLastName, String courseName, LocalDate startDate, LocalDate endDate, Integer numberOfGradedAssignments, Float averageScore, String letterGrade) {
        this.teacherLastName = teacherLastName;
        this.courseName = courseName;
        this.startDate = startDate;
        this.endDate = endDate;
        this.numberOfGradedAssignments = numberOfGradedAssignments;
        this.averageScore = averageScore;
        this.letterGrade = letterGrade;
    }

    public Long getStudentId() {
        return studentId;
    }

    public void setStudentId(Long studentId) {
        this.studentId = studentId;
    }

    public String getCourseName() {
        return courseName;
    }

    public void setCourseName(String courseName) {
        this.courseName = courseName;
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
