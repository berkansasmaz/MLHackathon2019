import {
	http
  } from "utils/http";
  
  const MonitoringService = {
	async olumluList(link) {
	  var result = await http.get("http://localhost:5000/olumluyorumlar?link=" + link);
	  if (result.status === 200) {
		return result.data;
	  } else {
		console.error(result.error);
		throw result.error;
	  }
	},
	async olumsuzList(link) {
		var result = await http.get("http://localhost:5000/olumsuzyorumlar?link=" + link);
		if (result.status === 200) {
		  return result.data;
		} else {
		  console.error(result.error);
		  throw result.error;
		}
	  },
	  async predict(link) {
		var result = await http.post("http://127.0.0.1:5000/predict?link=" +  link);
		
		if (result.status === 200) {
		  return result.data;
		} else {
		  console.error(result.error);
		  throw result.error;
		}
	  }
  }
  
  export default MonitoringService;