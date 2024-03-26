package com.flynn.schooldb.entity;

import java.util.List;

import jakarta.persistence.*;

@Entity
@Table(name = "staff")
public class Staff {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "staff_id")
    private Long staffId;

    @Column(name = "first_name", nullable = false)
    private String firstName;

    @Column(name = "middle_name")
    private String middleName;

    @Column(name = "last_name", nullable = false)
    private String lastName;

    @Column(name = "email", nullable = false)
    private String email;

    @Column(name = "position")
    private String position;

    @OneToMany(mappedBy = "staff", fetch = FetchType.LAZY, cascade = CascadeType.ALL)
    private List<StaffGradeLevel> staffGradeLevels;

    public Staff() {

    }

    public Staff(Long staffId, String firstName, String middleName, String lastName, String email, String position) {
        this.staffId = staffId;
        this.firstName = firstName;
        this.middleName = middleName;
        this.lastName = lastName;
        this.email = email;
        this.position = position;
    }

    public Long getStaffId() {
        return staffId;
    }

    public void setStaffId(Long staffId) {
        this.staffId = staffId;
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public List<StaffGradeLevel> getStaffGradeLevels() {
        return staffGradeLevels;
    }

    public void setStaffGradeLevels(List<StaffGradeLevel> staffGradeLevels) {
        this.staffGradeLevels = staffGradeLevels;
    }

    @Override
    public String toString() {
        return "Staff [staffId=" + staffId + ", firstName=" + firstName + ", middleName=" + middleName + ", lastName="
                + lastName + ", email=" + email + ", position=" + position + "]";
    }


}
