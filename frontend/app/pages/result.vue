<script setup lang="ts">
import type { result } from "~/models/result";

const predictionResult = useState<result>("predictionResult");
</script>

<template>
  <div>
    <h1>Resultado</h1>
    <p v-if="predictionResult">
      Diabetes: {{ predictionResult.diabetic ? "Sim" : "Não" }}
    </p>
    <p v-if="predictionResult">
      Probabilidade: {{ predictionResult.probability * 100 }}%
    </p>
  </div>
</template>
