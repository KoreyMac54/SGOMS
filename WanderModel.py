#note that for this model to run, world_size and number_of_agents must be set to non 0 values, 
#and the scripts must have access to the CCMsuite library (included in this repo), created by Terry Stewart & Rob West

world_size=0
world_x_range=world_size
world_y_range=world_size
number_of_agents=0

import sys
import os
sys.path.append(os.getcwd() + '\\CCMSuite')

import ccm
log=ccm.log(html=False)   
from ccm.lib.actr import *  

import random

goal_square = str(random.choice(range(world_x_range))), str(random.choice(range(world_y_range)))
pass#print goal_square
agent_list = []

class Environment(ccm.Model):        # items in the environment look and act like chunks - but note the syntactic differences
    prepping_world = True

    while prepping_world:
        occupied_tally = 0
        squares = [ccm.Model(isa='square', x=x, y=y, occupied=0, occupant='nil') \
            for x in range(world_x_range) for y in range(world_y_range)]
        
        for square in squares:
            if (str(square.x), str(square.y)) == goal_square:
                square.occupied = 1
                square.occupant = 'goal'
                
        for square in squares:
            x = random.choice(range(10))
            if x == 3 and \
                (str(square.x), str(square.y)) != goal_square:
                square.occupant = 'monster'
                square.occupied = 1

            elif x == 2 and \
                (str(square.x), str(square.y)) != goal_square:
                square.occupant = 'bunny'
                square.occupied = 1

        for s in squares:
            if s.occupied == 1:
                occupied_tally += 1
        if occupied_tally + number_of_agents >= world_x_range * world_y_range:
            continue
        else: 
            prepping_world = False


    agent_list = []

class MotorModule(ccm.ProductionSystem):     # create a motor module do the actions 
    #directions: 0 = up, 1 = right, 2 = down, 3 = left
    production_time = 0.05

    def moveForward(self):
        pass#print self.parent.instance_name, 'is trying to move forward'
        if self.parent.facing == 0:
            target_value = self.parent.y_coordinate - 1
            target_x_y = self.parent.x_coordinate, target_value
            if self.parent.y_coordinate >  0:
                for s in self.parent.parent.squares:
                    if (s.x, s.y) == target_x_y:
                        target_square = s
                        if s.occupied == '1':
                            pass#print 'cannot pass: square occupied'
                            pass
                        else:
                            pass#print 'target square is unoccupied'
                            pass#print self.parent.instance_name, ' moved forward to target'
                            pass#print '-1y'
                            self.parent.y_coordinate -= 1         
            else: 
                pass#print self.parent.instance_name, ' at edge of map; cannot move forward'
                pass

        elif self.parent.facing == 1:
            target_value = self.parent.x_coordinate + 1
            target_x_y = target_value, self.parent.y_coordinate
            if self.parent.x_coordinate < world_x_range:
                for s in self.parent.parent.squares:
                    if (s.x, s.y) == target_x_y:
                        target_square = s
                        if s.occupied == '1':
                            pass#print 'cannot pass: must engage monster first'
                            pass
                        else:
                            pass#print 'target square is unoccupied'
                            pass#print self.parent.instance_name, ' moved forward to target'
                            pass#print '+1x'
                            self.parent.x_coordinate += 1         
            else: 
                pass#print self.parent.instance_name, ' at edge of map; cannot move forward'
                pass

        elif self.parent.facing == 2:
            target_value = self.parent.y_coordinate + 1
            target_x_y = self.parent.x_coordinate, target_value
            if self.parent.y_coordinate < world_y_range:
                for s in self.parent.parent.squares:
                    if (s.x, s.y) == target_x_y:
                        target_square = s
                        if s.occupied == '1':
                            pass#print 'cannot pass: must engage monster first'
                            pass
                        else:
                            pass#print 'target square is unoccupied'
                            pass#print self.parent.instance_name, ' moved forward to target'
                            pass#print '-1y'
                            self.parent.y_coordinate += 1         
            else: 
                pass#print self.parent.instance_name, ' at edge of map; cannot move forward'
                pass
        elif self.parent.facing == 3:
            target_value = self.parent.x_coordinate - 1
            target_x_y = target_value, self.parent.y_coordinate
            if self.parent.x_coordinate > 0:
                for s in self.parent.parent.squares:
                    if (s.x, s.y) == target_x_y:
                        target_square = s
                        if s.occupied == '1':
                            pass#print 'cannot pass: must engage monster first'
                            pass
                        else:
                            pass#print 'target square is unoccupied'
                            pass#print self.parent.instance_name, ' moved forward to target'
                            pass#print '-1x'
                            self.parent.x_coordinate -= 1         
            else: 
                pass#print self.parent.instance_name, ' at edge of map; cannot move forward'
                pass

    def turnLeft(self):
        pass#print self.parent.instance_name, ' is turning left'
        if self.parent.facing == 0:
            self.parent.facing = 3
        else:
            self.parent.facing -= 1
        pass#print 'turned left'
    def turnRight(self):
        pass#print self.parent.instance_name, ' is turning right'
        if self.parent.facing == 3:
            self.parent.facing = 0
        else:
            self.parent.facing += 1
        pass#print 'turned right'
        
##navigation methods to approach known target
    def faceGoalY(self):
        pass#print 'running faceGoalY'
        if self.parent.y_coordinate == int(goal_square[1]):
            pass
        elif self.parent.y_coordinate < int(goal_square[1]):
            if self.parent.facing == 2:
                pass
            elif self.parent.facing == 1:
                self.parent.motor.turnRight()
            elif self.parent.facing == 3:
                self.parent.motor.turnLeft()
            elif self.parent.facing == 0:
                self.parent.motor.turnRight()
                self.parent.motor.turnRight()
        elif self.parent.y_coordinate > int(goal_square[1]):
            if self.parent.facing == 2:
                self.parent.motor.turnRight()
                self.parent.motor.turnRight()
            elif self.parent.facing == 1:
                self.parent.motor.turnLeft()
            elif self.parent.facing == 3:
                self.parent.motor.turnRight()
            elif self.parent.facing == 0:
                pass

    def approachGoal_Y(self):
        pass#print 'running approachGoal Y'
        
        if self.parent.y_coordinate == int(goal_square[1]):
            pass
        else: 
            delta_y = self.parent.y_coordinate - int(goal_square[1])
            for i in range(abs(delta_y)):
                self.parent.motor.moveForward()
                yield 0.05

    def faceGoalX(self):
        pass#print 'running faceGoalX'
        if self.parent.x_coordinate == int(goal_square[0]):
            pass
        elif self.parent.x_coordinate < int(goal_square[0]):
            if self.parent.facing == 0:
                self.parent.motor.turnRight()
            elif self.parent.facing == 1:
                pass
            elif self.parent.facing == 2:
                self.parent.motor.turnLeft()
            elif self.parent.facing == 3:
                self.parent.motor.turnRight()
                self.parent.motor.turnRight()
        elif self.parent.x_coordinate > int(goal_square[0]):
            if self.parent.facing == 0:
                self.parent.motor.turnLeft()
            elif self.parent.facing == 1:
                self.parent.motor.turnRight()
                self.parent.motor.turnRight()
            elif self.parent.facing == 2:
                self.parent.motor.turnRight()
            elif self.parent.facing == 3:
                pass

    def approachGoal_X(self):
        pass#print 'running approachGoal X'
        if self.parent.x_coordinate == int(goal_square[0]):
            pass
        else:
            delta_x = self.parent.x_coordinate - int(goal_square[0])
            for i in range(abs(delta_x)):
                self.parent.motor.moveForward()
                yield 0.05

    # def motor_idle_waiting(self):
    #     yield 1
    #     self.parent.focus_buffer.set('waiting_for_teammate')

class Top_Down_Vision_Module(ccm.ProductionSystem):
    production_time = 0.05

    def check_self_location(self):
        visual_string_temp = str('x_loc:' + str(self.parent.x_coordinate) \
            + ' y_loc:' + str(self.parent.y_coordinate) + ' facing:' + str(self.parent.facing))
        self.parent.visual_buffer.set(visual_string_temp)
        pass#print 'in ', self.parent.instance_name, '\'s visual buffer is', self.parent.visual_buffer.chunk
           
    def line_of_sight_constructor(self):
        #line_of_sight_vector = squares in front of the agent, to edge of map
        pass#print self.parent.instance_name, ' is at: ', self.parent.x_coordinate, self.parent.y_coordinate

        if self.parent.facing == 0:
            line_of_sight_vector = [s for s in env.squares if \
                s.x == self.parent.x_coordinate and s.y < self.parent.y_coordinate]
        elif self.parent.facing == 1:
            line_of_sight_vector = [s for s in env.squares if \
                s.y == self.parent.y_coordinate and s.x > self.parent.x_coordinate]
        elif self.parent.facing == 2:
            line_of_sight_vector = [s for s in env.squares if \
                s.x == self.parent.x_coordinate and s.y > self.parent.y_coordinate]
        elif self.parent.facing == 3:
            line_of_sight_vector = [s for s in env.squares if \
                s.y == self.parent.y_coordinate and s.x < self.parent.x_coordinate]

        for i in range(len(line_of_sight_vector)):
            if line_of_sight_vector[i].occupant == 'monster':
                line_of_sight_vector = line_of_sight_vector[0:i+1]
                ##^^ this causes the agent to see only up to the first obstruction (ie, monster)
                break
        pass#print self.parent.instance_name, ' LoS vector is ...', line_of_sight_vector
        for s in line_of_sight_vector:pass#print s.x, s.y

        self.parent.line_of_sight = line_of_sight_vector

    def update_top_down_vision(self):
        for square in self.parent.line_of_sight:
            if square.occupant == 'goal':
                self.parent.visual_buffer.set('goal:visible')
            elif square.occupant == 'monster' or square.occupant == 'bunny':
                self.parent.visual_buffer.set(square)

    def check_goal(self):
        pass#print self.parent.instance_name, ' checking goal'    
        if str(self.parent.x_coordinate) == goal_square[0] and \
            str(self.parent.y_coordinate) == goal_square[1]:
                pass#print self.parent.instance_name, ' goal conditions match'
                pass#print self.parent.instance_name, ' reached the goal!!!!'
                self.parent.focus_buffer.set('at_goal')
        else:
            pass#print 'not yet at goal'

    def vision_update(self):  #wraps all vision methods, calls them all together
        self.parent.top_down_vision.check_self_location()
        self.parent.top_down_vision.line_of_sight_constructor()
        self.parent.top_down_vision.update_top_down_vision()
        self.parent.top_down_vision.check_goal()

class Bottom_Up_Vision_Module(ccm.ProductionSystem):
    production_time = 0.05
    
    def monsterSpotting(DMbuffer='planning_unit:!kill_monster', visual_buffer='occupant:monster', DM='busy:False', unit_task_buffer=''):
        pass#print 'monster spotted'
        pass#print self.parent.instance_name, 'initiating monster slaying protocol'
        DM.request('planning_unit:kill_monster')
        context_buffer.set('last_action:none')
        unit_task_buffer.clear()
    def bunnySpotting(DMbuffer='planning_unit:!kill_monster', visual_buffer='occupant:bunny', DM='busy:False', unit_task_buffer=''):
        pass#print 'bunny spotted; ignoring it'
        pass#print self.parent.instance_name, 'ignoring bunny'
        DM.request('planning_unit:wander')
        visual_buffer.clear()
        context_buffer.set('last_action:none')
        unit_task_buffer.clear()

        
#define agent properties/methods
class MyAgent(ACTR): 
    #import time
 
##class attributes: buffers, modules, variables   
    focus_buffer=Buffer()
    visual_buffer=Buffer()
    context_buffer=Buffer()
    unit_task_buffer=Buffer()

    DMbuffer=Buffer()   # create a buffer for the declarative memory (henceforth DM)
    DM=Memory(DMbuffer)#,latency=0.3, threshold=0) # create DM and connect it to its buffer 

    motor=MotorModule()
    top_down_vision=Top_Down_Vision_Module()
    bottom_up_vision = Bottom_Up_Vision_Module()
    moveList = [motor.moveForward, motor.turnLeft, motor.turnRight]
    line_of_sight = []
    #these set the class variable to the global variable; allows for agent positioning to be tied to world size
    world_x_range = world_x_range
    world_y_range = world_y_range
    goal_coord = goal_square
    finished = False
    placed = False

    def init():
        DM.add('planning_unit:wander UnitTask1:random_movement UnitTask2:conclude')
        DM.add('planning_unit:kill_monster UnitTask1:ready UnitTask2:aim UnitTask3:fire UnitTask4:conclude')
        #find an open square to place agent on
        while not self.placed:
            x = random.choice(range(world_x_range))
            y = random.choice(range(world_y_range))
            init_x_y = (x,y)
            for s in self.parent.squares:
                if (s.x, s.y) == (x,y):
                    init_square = s
                    if init_square.occupied == 1:
                        continue
                    elif init_square.occupied == 0:
                        self.x_coordinate = x 
                        self.y_coordinate = y 
                        self.placed = True
        self.facing = random.randint(0,3)
        initial_delta = (abs(self.x_coordinate - int(goal_coord[0])) + abs(self.y_coordinate - int(goal_coord[1])))
        self.log.delta=initial_delta
        top_down_vision.check_self_location()
        DM.request('planning_unit:!kill_monster')
        context_buffer.set('last_action:none')



    
#planning unit selection productions
    def start_planning_unit(DMbuffer='planning_unit:?planning_unit', context_buffer='last_action:none'):
        x = sorted(DMbuffer.chunk.keys())
        y = DMbuffer.chunk[x[0]]
        context_buffer.clear()
        unit_task_buffer.set(y)

    def continue_planning_unit(DMbuffer='planning_unit:?planning_unit', context_buffer='last_action:?last_action!none!conclude', DM='busy:False'):
        pass#print 'getting next planning unit'
        x = sorted(DMbuffer.chunk.keys())
        pass#print x
        a = [key for key,value in DMbuffer.chunk.items() if value==last_action]
        pass#print a
        nextUnitTask = x.index(a[0]) + 1
        pass#print nextUnitTask
        y = DMbuffer.chunk[x[nextUnitTask]]
        pass#print y
        context_buffer.clear()
        unit_task_buffer.set(y)

    def finish_planning_unit(DMbuffer='planning_unit:?planning_unit', context_buffer='last_action:conclude'):
        pass#print 'planning unit', planning_unit, 'finished'
        context_buffer.set('last_action:none')
        unit_task_buffer.clear()
        DM.request('planning_unit:?')

#sequential navigation unit tasks
    def approach_Y(unit_task_buffer='approach_Y'):
        motor.faceGoalY()
        motor.approachGoal_Y()
        top_down_vision.vision_update()
        unit_task_buffer.clear()
        context_buffer.set('last_action:approach_Y')

    def approach_X(unit_task_buffer='approach_X'):
        motor.faceGoalX()
        motor.approachGoal_X()
        top_down_vision.vision_update()
        unit_task_buffer.clear()
        context_buffer.set('last_action:approach_X')

#random movement navigation unit task
    def wander(unit_task_buffer='random_movement'):
        random.choice(moveList)()
        top_down_vision.vision_update()
        unit_task_buffer.clear()
        context_buffer.set('last_action:random_movement')


#monster killing unit tasks
    def ready(unit_task_buffer='ready'):
        if self.line_of_sight == []:
            pass#print self.instance_name, 'nothing in sight, passing on ready'
            DM.request('planning_unit:!kill_monster')
            context_buffer.set('last_action:none')
            unit_task_buffer.clear()
            visual_buffer.clear()
        else:
            for s in self.line_of_sight:
                if s.occupant == 'monster':
                    pass#print self.instance_name, 'preparing to engage enemey'
                    unit_task_buffer.clear()
                    context_buffer.set('last_action:ready')
        if all(s.occupant != 'monster' for s in self.line_of_sight):
            pass#print 'no monsters here; passing on ready'
            DM.request('planning_unit:!kill_monster')
            context_buffer.set('last_action:none')
            unit_task_buffer.clear()
            visual_buffer.clear()


    def aim(unit_task_buffer='aim'):
        pass#print self.instance_name, 'aiming weapon'
        unit_task_buffer.clear()
        context_buffer.set('last_action:aim')

    def fire(unit_task_buffer='fire'):
        pass#print self.instance_name, '- fire!!!!!!'
        for i in self.parent.squares:
            if (i.x, i.y) == (visual_buffer.chunk['x'], visual_buffer.chunk['y']):
                i.occupant='nil'
                i.occupied=0
                pass#print 'monster slain  x.x'
        unit_task_buffer.clear()
        context_buffer.set('last_action:fire')
        
#generic planning unit conclude unit task
    def conclude(unit_task_buffer='conclude', DMbuffer='planning_unit:?planning_unit'):
        pass#print 'concluding the planning unit', planning_unit
        top_down_vision.vision_update()
        unit_task_buffer.clear()
        context_buffer.set('last_action:conclude')
 
#goal confirmation productions
    def reached_goal(focus_buffer='at_goal'):
        pass#print self.instance_name, 'ending from focus buffer'
        unit_task_buffer.clear()
        DMbuffer.clear()
        context_buffer.clear()
        visual_buffer.clear()
        self.finished = True
        focus_buffer.set('waiting_for_teammate')

    def wait_for_teammate_to_finish(focus_buffer='waiting_for_teammate'):
        production_time = 0.1
        if all(a.finished == True for a in self.parent.agent_list):
            pass#print 'all agents have finished'
            self.stop()
        else: 
            pass#print self.instance_name, 'is waiting'
            pass#print self.parent.agent_list
            for a in self.parent.agent_list: pass#print a.finished

            focus_buffer.set('waiting_for_teammate')
            pass#print 'xxxxxxxxxxxxxxxxxxxxxxxx'

env=Environment()

for a,i in enumerate(range(number_of_agents)):
    a = MyAgent()
    a.instance_name = str('agent' + str(i))
    env.agent = a
    env.agent_list.append(a)
    env.agent.log = log

#ccm.log_everything(env)
env.run()

ccm.finished()  
