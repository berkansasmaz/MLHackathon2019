<template>
	<h4 class="font-weight-bold py-3 mb-4">
		<icon	v-if="icon"	:icon="icon" />	<span class="text-muted font-weight-light">{{ prefix }} / </span> {{ title }}
	</h4>	
</template>

<script>
  import service from "service/MLHackathonServer";
  import router from "@/router";
export default {
	props: {
		title: {
			"default": "title",
			"type" : String
		},
		prefix: {
			"default": "MLHackathon",
			"type" : String
		},
		icon: {
			"type" : String
		}
	}
}
</script>