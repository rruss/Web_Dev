import { Component, OnInit, OnDestroy } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service'
import { ITaskList, ITask } from '../shared/models/models' 

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit, OnDestroy {

  public task_lists: ITaskList[] = []
  public tasks: ITask[] = []
  public loading = false
  public interval

  constructor(private provider: ProviderService) { }

  ngOnInit() {
  	
  }

  getTaskList(): void{
    this.provider.getTaskLists().then(res => {
  		this.task_lists = res
  		setTimeout(() => {
  			this.loading = true  	
  		}, 1500)
  	})

  }

  getTasks(id: ITaskList){
  	this.provider.getTasks(id).then(res => {
  		this.tasks = res
  	})
  }

  ngOnDestroy() {
    clearInterval(this.interval);
  }

}