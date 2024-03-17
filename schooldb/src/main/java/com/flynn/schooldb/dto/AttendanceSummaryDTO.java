package com.flynn.schooldb.dto;

public class AttendanceSummaryDTO {

    long totalDays;
    long daysFullAttendance;
    long daysPartialExcusedAbsence;
    long daysPartialUnexcusedAbsence;
    long daysUnexcusedAbsence;
    long daysExcusedAbsence;
    double attendanceRate;

    public AttendanceSummaryDTO() {
    }

    public AttendanceSummaryDTO(long totalDays, long daysFullAttendance, long daysPartialExcusedAbsence, long daysPartialUnexcusedAbsence, long daysUnexcusedAbsence, long daysExcusedAbsence, double attendanceRate) {
        this.totalDays = totalDays;
        this.daysFullAttendance = daysFullAttendance;
        this.daysPartialExcusedAbsence = daysPartialExcusedAbsence;
        this.daysPartialUnexcusedAbsence = daysPartialUnexcusedAbsence;
        this.daysUnexcusedAbsence = daysUnexcusedAbsence;
        this.daysExcusedAbsence = daysExcusedAbsence;
        this.attendanceRate = attendanceRate;
    }

    @Override
    public String toString() {
        return "AttendanceSummaryDTO{" +
                "totalDays=" + totalDays +
                ", daysFullAttendance=" + daysFullAttendance +
                ", daysPartialExcusedAbsence=" + daysPartialExcusedAbsence +
                ", daysPartialUnexcusedAbsence=" + daysPartialUnexcusedAbsence +
                ", daysUnexcusedAbsence=" + daysUnexcusedAbsence +
                ", daysExcusedAbsence=" + daysExcusedAbsence +
                ", attendanceRate=" + attendanceRate +
                '}';
    }

    public long getTotalDays() {
        return totalDays;
    }

    public void setTotalDays(long totalDays) {
        this.totalDays = totalDays;
    }

    public long getDaysFullAttendance() {
        return daysFullAttendance;
    }

    public void setDaysFullAttendance(long daysFullAttendance) {
        this.daysFullAttendance = daysFullAttendance;
    }

    public long getDaysPartialExcusedAbsence() {
        return daysPartialExcusedAbsence;
    }

    public void setDaysPartialExcusedAbsence(long daysPartialExcusedAbsence) {
        this.daysPartialExcusedAbsence = daysPartialExcusedAbsence;
    }

    public long getDaysPartialUnexcusedAbsence() {
        return daysPartialUnexcusedAbsence;
    }

    public void setDaysPartialUnexcusedAbsence(long daysPartialUnexcusedAbsence) {
        this.daysPartialUnexcusedAbsence = daysPartialUnexcusedAbsence;
    }

    public long getDaysUnexcusedAbsence() {
        return daysUnexcusedAbsence;
    }

    public void setDaysUnexcusedAbsence(long daysUnexcusedAbsence) {
        this.daysUnexcusedAbsence = daysUnexcusedAbsence;
    }

    public long getDaysExcusedAbsence() {
        return daysExcusedAbsence;
    }

    public void setDaysExcusedAbsence(long daysExcusedAbsence) {
        this.daysExcusedAbsence = daysExcusedAbsence;
    }

    public double getAttendanceRate() {
        return attendanceRate;
    }

    public void setAttendanceRate(double attendanceRate) {
        this.attendanceRate = attendanceRate;
    }
}
