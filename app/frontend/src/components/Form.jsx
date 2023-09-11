import { useState, useEffect } from "react";
import SectorSelector from "./SectorSelector";
import styles from "../styles/form.module.css";
import { useMediaQuery } from "@react-hook/media-query";

export default function Form() {
  const BACKEND_ORIGIN = "http://149.50.129.173/backend/api";
  const [name, setName] = useState("");
  const [sectors, setSectors] = useState([]);
  const [agreeToTerms, setAgreeToTerms] = useState(false);
  const [formData, setFormData] = useState(null);
  const [editing, setEditing] = useState(false);
  const isMediumDevice = useMediaQuery("(min-width: 1100px)");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!name || sectors.length === 0 || !agreeToTerms) {
      alert("All fields are mandatory!");
      return;
    }

    if (editing) {
      var id = (await (await fetch(`${BACKEND_ORIGIN}/last-record`)).json()).id;
    }

    console.log(id);
    const url =
      editing && id
        ? `${BACKEND_ORIGIN}/data/${id}`
        : `${BACKEND_ORIGIN}/submit`;
    const method = editing && id ? "PATCH" : "POST";

    try {
      const response = await fetch(url, {
        method,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name,
          sectors,
          agree_to_terms: agreeToTerms,
        }),
      });

      const data = await response.json();

      if (response.status === 200 || response.status === 201) {
        setFormData({
          name,
          sectors,
          agree_to_terms: agreeToTerms,
        });
      } else {
        console.error(data.detail);
      }
    } catch (error) {
      console.error("Error submitting the data:", error);
    }
  };

  useEffect(() => {
    if (formData) {
      setName(formData.name);
      setSectors(formData.sectors);
      setAgreeToTerms(formData.agree_to_terms);
    }
  }, [formData]);

  return (
    <div
      style={
        formData && isMediumDevice
          ? {
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
            }
          : null
      }
    >
      <form className={styles.container} onSubmit={handleSubmit}>
        Please enter your name and pick the Sectors you are currently involved
        in.
        <div>
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div>
          <label>Sectors:</label>
          <SectorSelector
            selectedSectors={sectors}
            setSelectedSectors={setSectors}
          />
        </div>
        <div className={styles.agreeContainer}>
          <label className={styles.agreeLabel}>Agree to Terms:</label>
          <input
            type="checkbox"
            checked={agreeToTerms}
            onChange={(e) => setAgreeToTerms(e.target.checked)}
          />
        </div>
        <input type="submit" value="Save" />
      </form>

      {formData && (
        <div className={styles.submittedDataContainer}>
          <h3 className={styles.submittedDataHeader}>Submitted Data:</h3>
          <p className={styles.submittedDataItem}>Name: {formData.name}</p>
          <p className={styles.submittedDataItem}>
            Sectors: {formData.sectors.join(", ")}
          </p>
          <p className={styles.submittedDataItem}>
            Agree to Terms: {formData.agree_to_terms ? "Yes" : "No"}
          </p>
          <button
            className={styles.toggleButton}
            onClick={() => setEditing(!editing)}
          >
            {editing ? "Back to Post Data" : "Edit Data"}
          </button>
        </div>
      )}
    </div>
  );
}
