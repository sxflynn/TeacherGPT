package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.entity.GradeLevel;
import com.flynn.schooldb.service.GradeLevelService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.List;

@Controller
public class GradeLevelQueryResolver {

    @Autowired
    private GradeLevelService gradeLevelService;

    @QueryMapping
    public List<GradeLevel> gradeLevelListAll(){
        return gradeLevelService.gradeLevelListAll();
    }

}
