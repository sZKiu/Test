import { useEffect, useState } from "react";
import PropTypes from "prop-types";
import "../styles/sectorselector.module.css";

const SectorSelector = ({ selectedSectors, setSelectedSectors }) => {
  SectorSelector.propTypes = {
    selectedSectors: PropTypes.array.isRequired,
    setSelectedSectors: PropTypes.func.isRequired,
  };

  const BACKEND_ORIGIN = import.meta.env.VITE_BACKEND_ORIGIN;
  const [sectors, setSectors] = useState([]);

  useEffect(() => {
    fetch(`${BACKEND_ORIGIN}/sectors`)
      .then((response) => response.json())
      .then((data) => setSectors(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []); //eslint-disable-line

  const handleChange = (e) => {
    const selectedOptions = Array.from(
      e.target.selectedOptions,
      (option) => option.value
    );
    setSelectedSectors(selectedOptions);
  };

  const renderSubsectors = (subsectors, indent = "") => {
    return subsectors
      .map((subsector) => {
        const options = [
          <option
            key={subsector.id}
            value={subsector.id}
            dangerouslySetInnerHTML={{ __html: indent + subsector.name }}
          ></option>,
        ];

        if (subsector.subsectors) {
          options.push(
            renderSubsectors(subsector.subsectors, indent + "&nbsp;&nbsp;")
          );
        }

        return options;
      })
      .flat();
  };

  return (
    <select onChange={handleChange} multiple size={10} value={selectedSectors}>
      {sectors.map((sector) => (
        <optgroup key={sector.id} label={sector.name}>
          {renderSubsectors(sector.subsectors)}
        </optgroup>
      ))}
    </select>
  );
};

export default SectorSelector;
