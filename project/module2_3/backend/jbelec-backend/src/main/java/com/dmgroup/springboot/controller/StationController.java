package com.dmgroup.springboot.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.dmgroup.springboot.pojo.Station;
import com.dmgroup.springboot.service.StationService;;

@RestController
@RequestMapping("/station")
public class StationController {
	@Autowired
	private StationService stationService;
	
	@RequestMapping("/find/all")
	public List<Station> find(){
		return stationService.findAll();
	}
}
