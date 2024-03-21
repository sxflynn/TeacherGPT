package com.flynn.schooldb.entity;
import jakarta.persistence.*;

@Entity
@Table(name = "family_group")
public class FamilyGroup {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long familyGroupId;

    @ManyToOne
    @JoinColumn(name = "student_id")
    private Student student;

    @ManyToOne
    @JoinColumn(name = "family_member_id")
    private FamilyMember familyMember;

    @Column(name = "parent_guardian", nullable = false)
    private boolean parentGuardian;

    @Column(name = "emergency_pickup", nullable = false)
    private boolean emergencyPickup;

    @ManyToOne
    @JoinColumn(name = "relationship_type_id")
    private RelationshipType relationshipType;

    public FamilyGroup() {
    }

    public FamilyGroup(Long familyGroupId, Student student, FamilyMember familyMember, boolean parentGuardian, boolean emergencyPickup) {
        this.familyGroupId = familyGroupId;
        this.student = student;
        this.familyMember = familyMember;
        this.parentGuardian = parentGuardian;
        this.emergencyPickup = emergencyPickup;
    }

    @Override
    public String toString() {
        return "FamilyGroup{" +
                "id=" + familyGroupId +
                ", student=" + student +
                ", familyMember=" + familyMember +
                ", parentGuardian=" + parentGuardian +
                ", emergencyPickup=" + emergencyPickup +
                ", relationshipType=" + relationshipType +
                '}';
    }

    public Long getFamilyGroupId() {
        return familyGroupId;
    }

    public void setFamilyGroupId(Long familyGroupId) {
        this.familyGroupId = familyGroupId;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

    public FamilyMember getFamilyMember() {
        return familyMember;
    }

    public void setFamilyMember(FamilyMember familyMember) {
        this.familyMember = familyMember;
    }

    public boolean isParentGuardian() {
        return parentGuardian;
    }

    public void setParentGuardian(boolean parentGuardian) {
        this.parentGuardian = parentGuardian;
    }

    public boolean isEmergencyPickup() {
        return emergencyPickup;
    }

    public void setEmergencyPickup(boolean emergencyPickup) {
        this.emergencyPickup = emergencyPickup;
    }

    public RelationshipType getRelationshipType() {
        return relationshipType;
    }

    public void setRelationshipType(RelationshipType relationshipType) {
        this.relationshipType = relationshipType;
    }
}
