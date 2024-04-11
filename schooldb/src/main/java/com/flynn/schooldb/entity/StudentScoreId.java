package com.flynn.schooldb.entity;

import java.io.Serializable;

public class StudentScoreId implements Serializable {
    private Long studentId;
    private Long assignmentId;

    public StudentScoreId(Long studentId, Long assignmentId) {
        this.studentId = studentId;
        this.assignmentId = assignmentId;
    }

    public StudentScoreId() {
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

}
