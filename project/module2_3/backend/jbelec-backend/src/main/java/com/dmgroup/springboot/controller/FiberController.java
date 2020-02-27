package com.dmgroup.springboot.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.dmgroup.springboot.pojo.Fiber;
import com.dmgroup.springboot.service.FiberService;
@RestController
@RequestMapping("/fiber")
public class FiberController {

	@Autowired
	private FiberService fiberService;
	
	@RequestMapping("/find/all")
	public List<Fiber> find(){
		//System.out.println("here");
		return fiberService.findAll();
	}
	@RequestMapping("/find/one")
	public Fiber findone(){
		//System.out.println("here");
		return fiberService.getFiber(0);
	}
}