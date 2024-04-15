package com.flynn.schooldb.dto;

import com.flynn.schooldb.entity.Student;
import com.flynn.schooldb.util.GradeCalculator;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

public class ReportCardDTO {

    private Optional<Student> student;

    private List<CourseGradeDTO> allGradeSummaries;

    private Float gradeAverage;

    private LocalDate startDate;

    private LocalDate endDate;

    public ReportCardDTO() {
    }

    public ReportCardDTO(Optional<Student> student, List<CourseGradeDTO> allGradeSummaries, Float gradeAverage, LocalDate startDate, LocalDate endDate) {
        this.student = student;
        this.allGradeSummaries = allGradeSummaries;
        this.gradeAverage = gradeAverage;
        this.startDate = startDate;
        this.endDate = endDate;
    }

    public Optional<Student> getStudent() {
        return student;
    }

    public void setStudent(Optional<Student> student) {
        this.student = student;
    }

    public List<CourseGradeDTO> getAllGradeSummaries() {
        return allGradeSummaries;
    }

    public void setAllGradeSummaries(List<CourseGradeDTO> allGradeSummaries) {
        this.allGradeSummaries = allGradeSummaries;
    }

    public void setGradeAverage(Float gradeAverage) {
        this.gradeAverage = gradeAverage;
    }

    public String getGradeAverage() {
        return String.format("%.2f%%", gradeAverage * 100);
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


}
