package com.flynn.schooldb.entity;
import jakarta.persistence.*;

import java.time.LocalDate;
import java.util.List;


@Entity
@Table(name = "student")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "student_id")
    private Long studentId;

    @Column(name = "first_name", nullable = false)
    private String firstName;

    @Column(name = "middle_name")
    private String middleName;

    @Column(name = "last_name", nullable = false)
    private String lastName;

    @Column(name = "sex", length = 1)
    private Character sex;

    @Column(name = "dob", nullable = false)
    @Temporal(TemporalType.DATE)
    private LocalDate dob;

    @Column(name = "email", unique = true, nullable = false)
    private String email;

    @Column(name = "ohio_ssid", nullable = false, unique = true)
    private String ohioSsid;

    @OneToMany(mappedBy = "student", fetch = FetchType.LAZY, cascade = CascadeType.ALL)
    private List<DailyAttendance> dailyAttendance;

    public Student() {
    }

    public Student(String firstName, String middleName, String lastName, Character sex, LocalDate dob, String email, String ohioSsid) {
        this.firstName = firstName;
        this.middleName = middleName;
        this.lastName = lastName;
        this.sex = sex;
        this.dob = dob;
        this.email = email;
        this.ohioSsid = ohioSsid;
    }

    @Override
    public String toString() {
        return "Student{" +
                "studentId=" + studentId +
                ", firstName='" + firstName + '\'' +
                ", middleName='" + middleName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", sex=" + sex +
                ", dob=" + dob +
                ", email='" + email + '\'' +
                ", ohioSsid='" + ohioSsid + '\'' +
                ", dailyAttendance=" + dailyAttendance +
                '}';
    }

    public Long getStudentId() {
        return studentId;
    }

    public void setStudentId(Long studentId) {
        this.studentId = studentId;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getMiddleName() {
        return middleName;
    }

    public void setMiddleName(String middleName) {
        this.middleName = middleName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Character getSex() {
        return sex;
    }

    public void setSex(Character sex) {
        this.sex = sex;
    }

    public LocalDate getDob() {
        return dob;
    }

    public void setDob(LocalDate dob) {
        this.dob = dob;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getOhioSsid() {
        return ohioSsid;
    }

    public void setOhioSsid(String ohioSsid) {
        this.ohioSsid = ohioSsid;
    }

    public List<DailyAttendance> getDailyAttendance() {
        return dailyAttendance;
    }

    public void setDailyAttendance(List<DailyAttendance> dailyAttendance) {
        this.dailyAttendance = dailyAttendance;
    }
}
