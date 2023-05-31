{
  "process": {
    "process": "Process({'id': 'process'})",
    "height": 80,
    "elements": {
      "start": "Start({'id': 'start'})",
      "hello": "Task({'id': 'hello', 'name': 'Say \"Hello!\"'})",
      "wait": "Task({'id': 'wait', 'name': 'Wait for response...'})",
      "end": "End({'id': 'end'})"
    },
    "start": "Start({'id': 'start'})",
    "steps": {
      "start": [
        "hello"
      ],
      "hello": [
        "wait"
      ],
      "wait": [
        "end"
      ],
      "end": []
    },
    "end": "End({'id': 'end'})"
  }
}
<?xml version="1.0" encoding="utf-8"?>
<bpmn:definitions id="definitions" xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:bioc="http://bpmn.io/schema/bpmn/biocolor/1.0" xmlns:color="http://www.omg.org/spec/BPMN/non-normative/color/1.0">
	<bpmn:process id="process">
		<bpmn:sequenceFlow id="flow_start_hello" sourceRef="start" targetRef="hello"></bpmn:sequenceFlow>
		<bpmn:sequenceFlow id="flow_hello_wait" sourceRef="hello" targetRef="wait"></bpmn:sequenceFlow>
		<bpmn:sequenceFlow id="flow_wait_end" sourceRef="wait" targetRef="end"></bpmn:sequenceFlow>
		<bpmn:startEvent id="start">
			<bpmn:outgoing>flow_start_hello</bpmn:outgoing>
		</bpmn:startEvent>
		<bpmn:task id="hello" name='Say "Hello!"'>
			<bpmn:incoming>flow_start_hello</bpmn:incoming>
			<bpmn:outgoing>flow_hello_wait</bpmn:outgoing>
		</bpmn:task>
		<bpmn:task id="wait" name="Wait for response...">
			<bpmn:incoming>flow_hello_wait</bpmn:incoming>
			<bpmn:outgoing>flow_wait_end</bpmn:outgoing>
		</bpmn:task>
		<bpmn:endEvent id="end">
			<bpmn:incoming>flow_wait_end</bpmn:incoming>
		</bpmn:endEvent>
	</bpmn:process>
	<bpmn:collaboration id="collaboration">
		<bpmn:participant id="participant" name="lane" processRef="process"></bpmn:participant>
	</bpmn:collaboration>
	<bpmndi:BPMNDiagram id="diagram">
		<bpmndi:BPMNPlane id="plane_collaboration" bpmnElement="collaboration">
			<bpmndi:BPMNShape id="shape_participant" bpmnElement="participant" isHorizontal="true">
				<dc:Bounds x="160" y="80" height="125" width="447"></dc:Bounds>
			</bpmndi:BPMNShape>
			<bpmndi:BPMNShape id="shape_start" bpmnElement="start">
				<dc:Bounds x="215" y="127" height="36" width="36"></dc:Bounds>
			</bpmndi:BPMNShape>
			<bpmndi:BPMNShape id="shape_hello" bpmnElement="hello">
				<dc:Bounds x="281" y="105" height="80" width="100"></dc:Bounds>
				<bpmndi:BPMNLabel></bpmndi:BPMNLabel>
			</bpmndi:BPMNShape>
			<bpmndi:BPMNShape id="shape_wait" bpmnElement="wait">
				<dc:Bounds x="411" y="105" height="80" width="100"></dc:Bounds>
				<bpmndi:BPMNLabel></bpmndi:BPMNLabel>
			</bpmndi:BPMNShape>
			<bpmndi:BPMNShape id="shape_end" bpmnElement="end">
				<dc:Bounds x="541" y="127" height="36" width="36"></dc:Bounds>
			</bpmndi:BPMNShape>
			<bpmndi:BPMNEdge id="edge_flow_start_hello" bpmnElement="flow_start_hello">
				<di:waypoint x="251" y="145"></di:waypoint>
				<di:waypoint x="281" y="145"></di:waypoint>
			</bpmndi:BPMNEdge>
			<bpmndi:BPMNEdge id="edge_flow_hello_wait" bpmnElement="flow_hello_wait">
				<di:waypoint x="381" y="145"></di:waypoint>
				<di:waypoint x="411" y="145"></di:waypoint>
			</bpmndi:BPMNEdge>
			<bpmndi:BPMNEdge id="edge_flow_wait_end" bpmnElement="flow_wait_end">
				<di:waypoint x="511" y="145"></di:waypoint>
				<di:waypoint x="541" y="145"></di:waypoint>
			</bpmndi:BPMNEdge>
		</bpmndi:BPMNPlane>
	</bpmndi:BPMNDiagram>
</bpmn:definitions>
