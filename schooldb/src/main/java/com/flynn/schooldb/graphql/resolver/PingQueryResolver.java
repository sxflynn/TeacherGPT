package com.flynn.schooldb.graphql.resolver;
import com.flynn.schooldb.entity.DailyAttendance;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.List;

@Controller
public class PingQueryResolver {

    @QueryMapping
    public String ping() {
        return "Healthy";
    }
}
