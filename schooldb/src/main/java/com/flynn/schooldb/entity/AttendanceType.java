package com.flynn.schooldb.entity;

import jakarta.persistence.*;

@Entity
@Table(name="attendance_type")
public class AttendanceType {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="attendance_type_id")
    private Long attendanceTypeId;
    @Column(name = "attendance_type", nullable = false)
    private String attendanceType;

    public AttendanceType() {
    }

    public AttendanceType(String attendanceType) {
        this.attendanceType = attendanceType;
    }

    public Long getAttendanceTypeId() {
        return attendanceTypeId;
    }

    public void setAttendanceTypeId(Long attendanceTypeId) {
        this.attendanceTypeId = attendanceTypeId;
    }

    public String getAttendanceType() {
        return attendanceType;
    }

    public void setAttendanceType(String attendanceType) {
        this.attendanceType = attendanceType;
    }
}
