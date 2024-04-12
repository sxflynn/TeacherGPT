package com.flynn.schooldb.dto;

import com.flynn.schooldb.entity.Course;
import com.flynn.schooldb.entity.Student;
import com.flynn.schooldb.util.LetterGrade;

import java.time.LocalDate;

public class CourseGradeDTO {

    private Student student;

    private Course course;

    private LocalDate startDate;

    private LocalDate endDate;

    private Float averageScore;

    private String letterGrade;

    public CourseGradeDTO() {
    }
    public CourseGradeDTO(Student student, Course course, LocalDate startDate, LocalDate endDate, Float averageScore, String letterGrade) {
        this.student = student;
        this.course = course;
        this.startDate = startDate;
        this.endDate = endDate;
        this.averageScore = averageScore;
        this.letterGrade = letterGrade;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
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

    public Float getAverageScore() {
        return averageScore;
    }

    public void setAverageScore(Float averageScore) {
        this.averageScore = averageScore;
        this.letterGrade = LetterGrade.toLetterGrade(averageScore.intValue());
    }

    public String getLetterGrade() {
        return letterGrade;
    }

}
