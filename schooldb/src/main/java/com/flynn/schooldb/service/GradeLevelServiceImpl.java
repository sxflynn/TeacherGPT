package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.GradeLevel;
import com.flynn.schooldb.repository.GradeLevelRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class GradeLevelServiceImpl implements GradeLevelService {

    private final GradeLevelRepository gradeLevelRepository;

    @Autowired
    public GradeLevelServiceImpl(GradeLevelRepository gradeLevelRepository) {
        this.gradeLevelRepository = gradeLevelRepository;
    }

    @Override
    public List<GradeLevel> gradeLevelListAll() {
        return gradeLevelRepository.findAll();
    }
}
