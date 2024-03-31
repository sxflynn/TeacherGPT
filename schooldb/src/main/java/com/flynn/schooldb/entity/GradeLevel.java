package com.flynn.schooldb.entity;

import java.util.List;

import jakarta.persistence.*;

@Entity
@Table(name="grade_levels")
public class GradeLevel {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "grade_level_id")
    private Long gradeLevelId;

    @Column(name = "grade_level_name", nullable = false)
    private String gradeLevelName;

    @OneToOne
    @JoinColumn(name = "grade_level_chair", nullable = false, unique = true)
    private Staff gradeLevelChair;

    @OneToMany(mappedBy = "gradeLevel", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Student> students;

    @ManyToMany
    @JoinTable(
      name = "staff_grade_levels",
      joinColumns = @JoinColumn(name = "grade_level_id"),
      inverseJoinColumns = @JoinColumn(name = "staff_id")
    )
    private List<Staff> staffMembers;
     
    public GradeLevel (){
    }

    public GradeLevel(Long gradeLevelId, String gradeLevelName, Staff gradeLevelChair) {
        this.gradeLevelId = gradeLevelId;
        this.gradeLevelName = gradeLevelName;
        this.gradeLevelChair = gradeLevelChair;
    }

    public Long getGradeLevelId() {
        return gradeLevelId;
    }

    public void setGradeLevelId(Long gradeLevelId) {
        this.gradeLevelId = gradeLevelId;
    }

    public String getGradeLevelName() {
        return gradeLevelName;
    }

    public void setGradeLevelName(String gradeLevelName) {
        this.gradeLevelName = gradeLevelName;
    }

    public Staff getGradeLevelChair() {
        return gradeLevelChair;
    }

    public void setGradeLevelChair(Staff gradeLevelChair) {
        this.gradeLevelChair = gradeLevelChair;
    }

    @Override
    public String toString() {
        return "GradeLevel [gradeLevelId=" + gradeLevelId + ", gradeLevelName=" + gradeLevelName + ", gradeLevelChair="
                + gradeLevelChair + "]";
    }
    

}
