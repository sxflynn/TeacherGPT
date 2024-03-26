package com.flynn.schooldb.entity;
import jakarta.persistence.*;

@Entity
@Table(name = "staff_grade_levels")
public class StaffGradeLevel {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // not in the database table

    @ManyToOne
    @JoinColumn(name = "grade_level_id")
    private GradeLevel gradeLevel;

    @ManyToOne
    @JoinColumn(name = "staff_id")
    private Staff staff;

    public StaffGradeLevel() {
    }

    public StaffGradeLevel(Long id, GradeLevel gradeLevel, Staff staff) {
        this.id = id;
        this.gradeLevel = gradeLevel;
        this.staff = staff;
    }

    public GradeLevel getGradeLevel() {
        return gradeLevel;
    }

    public void setGradeLevel(GradeLevel gradeLevel) {
        this.gradeLevel = gradeLevel;
    }

    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }

    @Override
    public String toString() {
        return "StaffGradeLevel [gradeLevel=" + gradeLevel + ", staff=" + staff + "]";
    }

}
