package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.RelationshipType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RelationshipTypeRepository extends JpaRepository<RelationshipType, Long> {
    List<RelationshipType> findAll();

}
