<script setup lang="ts">
import { z } from "zod";
import type { FormSubmitEvent } from "#ui/types";
import type { diabetes_prediction } from "../models/diabetes_prediction";
import FormWrapper from "../components/FormWrapper.vue";
import type { result } from "~/models/result";

const predictionResult = useState<result | null>(
  "predictionResult",
  () => null
);

const schema = z.object({
  gender: z.number().nonnegative().gte(0),
  age: z.number().int(),
  blood_glucose_level: z.number().int().positive(),
  hypertension: z.boolean(),
  heart_disease: z.boolean(),
  bmi: z.number().positive(),
  hba1c_level: z.number().positive(),
});

type Schema = z.output<typeof schema>;

const state = reactive<diabetes_prediction>({
  gender: -1,
  age: 0,
  blood_glucose_level: 0,
  bmi: 0,
  hba1c_level: 0,
  hypertension: false,
  heart_disease: false,
});

const genders = [
  { label: "Female", value: 0 },
  { label: "Male", value: 1 },
];

async function onSubmit(event: FormSubmitEvent<Schema>) {
  const { data, error } = await useFetch<result>(
    "http://localhost:8000/api/predict",
    {
      method: "POST",
      body: event.data,
    }
  );

  if (error.value) {
    console.error("Erro na requisição:", error.value);
    return;
  }

  predictionResult.value = data.value as result;
  navigateTo("result");
}
</script>

<template>
  <div class="w-dvw h-dvh flex justify-center items-center">
    <UForm
      :schema="schema"
      :state="state"
      class="space-y-4 p-6 w-full max-w-lg flex flex-col justify-center items-center"
      @submit="onSubmit"
    >
      <UFormField class="w-full" label="Gender" name="gender">
        <USelect
          v-model="state.gender"
          class="w-full"
          placeholder="No gender selected"
          :items="genders"
        />
      </UFormField>

      <FormWrapper>
        <UFormField class="w-full" label="Age" name="age">
          <UInput v-model="state.age" input-class="teste223w23" type="number" />
        </UFormField>

        <UFormField
          class="w-full"
          label="Blood glucose level"
          name="blood_glucose_level"
        >
          <UInput v-model="state.blood_glucose_level" type="number" />
        </UFormField>
      </FormWrapper>

      <FormWrapper>
        <UFormField class="w-full" label="BMI" name="bmi">
          <UInput v-model="state.bmi" type="number" />
        </UFormField>

        <UFormField class="w-full" label="hbA1c level" name="hba1c_level">
          <UInput v-model="state.hba1c_level" type="number" />
        </UFormField>
      </FormWrapper>

      <FormWrapper>
        <UFormField class="w-full" name="hypertension">
          <UCheckbox
            v-model="state.hypertension"
            name="hypertension"
            label="Do you have hypertension?"
          />
        </UFormField>

        <UFormField class="w-full" name="heart_disease">
          <UCheckbox
            v-model="state.heart_disease"
            name="heart_disease"
            label="Do you have heart disease?"
          />
        </UFormField>
      </FormWrapper>

      <UButton class="w-fit" type="submit"> Submit </UButton>
    </UForm>
  </div>
</template>
