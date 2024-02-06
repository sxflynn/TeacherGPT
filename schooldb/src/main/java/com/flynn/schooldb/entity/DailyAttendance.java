package com.flynn.schooldb.entity;
import jakarta.persistence.*;
import java.time.LocalDate;
import java.time.OffsetDateTime;

@Entity
@Table(name = "daily_attendance")
public class DailyAttendance {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "daily_attendance_id")
    private Long dailyAttendanceId;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "student_id")
    private Student student;

    private LocalDate date;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "attendance_type_id")
    private AttendanceType attendanceType;

    @Column(name = "arrival")
    private OffsetDateTime arrival;

    @Column(name = "departure")
    private OffsetDateTime departure;

    @Column(name = "excuse_note")
    private String excuseNote;


    public DailyAttendance() {
    }

    public DailyAttendance(Student student, LocalDate date, AttendanceType attendanceType, OffsetDateTime arrival, OffsetDateTime departure, String excuseNote) {
        this.student = student;
        this.date = date;
        this.attendanceType = attendanceType;
        this.arrival = arrival;
        this.departure = departure;
        this.excuseNote = excuseNote;
    }

    @Override
    public String toString() {
        return "DailyAttendance{" +
                "dailyAttendanceId=" + dailyAttendanceId +
                ", student=" + student +
                ", date=" + date +
                ", attendanceType=" + attendanceType +
                ", arrival=" + arrival +
                ", departure=" + departure +
                ", excuseNote='" + excuseNote + '\'' +
                '}';
    }

    public Long getDailyAttendanceId() {
        return dailyAttendanceId;
    }

    public void setDailyAttendanceId(Long dailyAttendanceId) {
        this.dailyAttendanceId = dailyAttendanceId;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public AttendanceType getAttendanceType() {
        return attendanceType;
    }

    public void setAttendanceType(AttendanceType attendanceType) {
        this.attendanceType = attendanceType;
    }

    public OffsetDateTime getArrival() {
        return arrival;
    }

    public void setArrival(OffsetDateTime arrival) {
        this.arrival = arrival;
    }

    public OffsetDateTime getDeparture() {
        return departure;
    }

    public void setDeparture(OffsetDateTime departure) {
        this.departure = departure;
    }

    public String getExcuseNote() {
        return excuseNote;
    }

    public void setExcuseNote(String excuseNote) {
        this.excuseNote = excuseNote;
    }
}
