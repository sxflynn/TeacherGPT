package com.flynn.schooldb.entity;
import jakarta.persistence.*;

import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "relationship_type")
public class RelationshipType {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "relationship_type_id")
    private Long relationshipTypeId;

    @Column(name = "relationship_type", nullable = false)
    private String relationshipType;

    @OneToMany(mappedBy = "relationshipType")
    private Set<FamilyGroup> familyGroups = new HashSet<>();

    public RelationshipType() {
    }

    public RelationshipType(Long id, String relationshipType) {
        this.relationshipTypeId = id;
        this.relationshipType = relationshipType;
    }

    @Override
    public String toString() {
        return "RelationshipType{" +
                "id=" + relationshipTypeId +
                ", relationshipType='" + relationshipType + '\'' +
                '}';
    }

    public Long getRelationshipTypeId() {
        return relationshipTypeId;
    }

    public void setRelationshipTypeId(Long relationshipTypeId) {
        this.relationshipTypeId = relationshipTypeId;
    }

    public String getRelationshipType() {
        return relationshipType;
    }

    public void setRelationshipType(String relationshipType) {
        this.relationshipType = relationshipType;
    }
}
