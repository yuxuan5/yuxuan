package com.dmgroup.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@SpringBootApplication // ��ʾ����һ��springbootӦ�ã����������������ͻ�����tomcatĬ�϶˿�8080
@EnableCaching // open caching
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
