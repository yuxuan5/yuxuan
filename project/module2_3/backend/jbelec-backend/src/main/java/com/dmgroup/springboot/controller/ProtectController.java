package com.dmgroup.springboot.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.dmgroup.springboot.pojo.Protect;
import com.dmgroup.springboot.service.ProtectService;

@RestController
@RequestMapping("/protect")
public class ProtectController {
	@Autowired
	private ProtectService protectService;
	
	@RequestMapping("/find/all")
	public List<Protect> find(){
		return protectService.findAll();
	}
}
